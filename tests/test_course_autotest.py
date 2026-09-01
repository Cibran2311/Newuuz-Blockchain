from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from gspread.exceptions import WorksheetNotFound

from scripts.course_autotest import (
    A2_PASS_COMPLEXITY,
    Assignment1Config,
    Assignment1Result,
    EthernautResult,
    GitHubHelper,
    SubmissionResult,
    Student,
    WorkOutcome,
    WorkSubmission,
    build_work_outcomes,
    check_ethernaut,
    evaluate_assignment1_transfers,
    find_erc721_approval,
    fetch_student_submission,
    overall_status,
    parse_submission_document,
    read_assignment1_config_from_google_sheet,
    read_ethernaut_config_from_google_sheet,
    read_students_from_google_sheet,
    selected_work_ids,
    write_google_results,
)


class FakeWorksheet:
    def __init__(self, rows):
        self.rows = rows

    def get_all_records(self, default_blank=""):
        return self.rows


class FakeSpreadsheet:
    def __init__(self, sheets):
        self.sheets = sheets

    def worksheet(self, name):
        return FakeWorksheet(self.sheets[name])


class FakeClient:
    def __init__(self, sheets):
        self.spreadsheet = FakeSpreadsheet(sheets)

    def open_by_key(self, key):
        return self.spreadsheet


class FakeOutputWorksheet:
    def __init__(self, title, sheet_id):
        self.title = title
        self.id = sheet_id
        self.values = []

    def update_title(self, title):
        self.title = title

    def resize(self, rows, cols):
        self.size = (rows, cols)

    def update(self, values, range_name, value_input_option):
        self.values = values

    def get_all_values(self):
        return self.values

    def append_row(self, values, value_input_option):
        self.values.append(values)


class FakeOutputSpreadsheet:
    def __init__(self):
        self.id = "result-sheet-id"
        self.sheet1 = FakeOutputWorksheet("Sheet1", 1)
        self.worksheets = [self.sheet1]

    def worksheet(self, title):
        for worksheet in self.worksheets:
            if worksheet.title == title:
                return worksheet
        raise WorksheetNotFound(title)

    def add_worksheet(self, title, rows, cols):
        worksheet = FakeOutputWorksheet(title, len(self.worksheets) + 1)
        self.worksheets.append(worksheet)
        return worksheet

    def batch_update(self, body):
        pass


class FakeOutputClient:
    def __init__(self):
        self.opened = None
        self.spreadsheet = FakeOutputSpreadsheet()

    def open_by_key(self, spreadsheet_id):
        self.opened = spreadsheet_id
        return self.spreadsheet


class CourseAutotestTests(unittest.TestCase):
    def test_submission_reader_requires_exact_repository_url(self):
        student = Student(
            "Ada", "101", "https://github.com/ada", ["0x" + "1" * 40]
        )
        github = MagicMock()

        result = fetch_student_submission(student, github)

        self.assertEqual(result.status, "INVALID REPORT")
        self.assertIn("exact GitHub repository URL", result.note)
        github.get_repo.assert_not_called()

    def test_submission_json_requires_exact_student_id(self):
        document = {
            "schema_version": 2,
            "student_id": "TEST-001",
            "labs": {
                f"lab{number}": {
                    "status": "draft",
                    "network": "testnet",
                    "evidence": {},
                    "links": [],
                    "answers": {},
                    "notes": "",
                }
                for number in range(1, 13)
            },
            "assignments": {
                f"assignment{number}": {
                    "status": "draft",
                    "network": "testnet",
                    "evidence": {},
                    "links": [],
                    "answers": {},
                    "notes": "",
                }
                for number in range(1, 5)
            },
        }

        import json

        version, works = parse_submission_document(
            json.dumps(document), expected_student_id="TEST-001"
        )
        self.assertEqual(version, 2)
        self.assertEqual(len(works), 16)
        with self.assertRaisesRegex(ValueError, "student_id mismatch"):
            parse_submission_document(
                json.dumps(document), expected_student_id="TEST-002"
            )

    def test_scopes_keep_all_twelve_labs_and_four_assignments(self):
        self.assertEqual(len(selected_work_ids("labs")), 12)
        self.assertEqual(len(selected_work_ids("assignments")), 4)
        self.assertEqual(len(selected_work_ids("all")), 16)
        self.assertEqual(selected_work_ids("lab7"), ("lab7",))

    def test_unimplemented_work_is_reviewed_but_assignment1_can_pass(self):
        student = Student(
            "Ada", "101", "https://github.com/ada/course", ["0x" + "1" * 40]
        )
        submission = SubmissionResult(
            status="VALID",
            repository="ada/course",
            commit_sha="a" * 40,
            works={
                "lab7": WorkSubmission(status="submitted", network="sepolia"),
                "assignment1": WorkSubmission(
                    status="submitted", network="sepolia"
                ),
            },
        )

        outcomes = build_work_outcomes(
            students=[student],
            selected=("lab7", "assignment1"),
            submissions={"101": submission},
            a1_results={"101": Assignment1Result(status="PASS")},
            a2_results={},
        )["101"]

        self.assertEqual(outcomes["lab7"].final_status, "REVIEW")
        self.assertEqual(outcomes["assignment1"].final_status, "PASS")

    def test_reads_only_active_students_and_normalizes_id(self):
        client = FakeClient(
            {
                "COURSE_STUDENTS": [
                    {
                        "Name": "Ada",
                        "ID": 101.0,
                        "Email": "ada@example.edu",
                        "GitHub": "https://github.com/ada",
                        "Ethereum": "0x" + "1" * 40,
                        "Polkadot": "5Ada",
                        "TON": "kQAda",
                        "Group": "G1",
                        "Active": "yes",
                    },
                    {"Name": "Inactive", "ID": 102, "Active": "false"},
                ]
            }
        )

        students = read_students_from_google_sheet(
            client, "sheet-id", "COURSE_STUDENTS"
        )

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].student_id, "101")
        self.assertEqual(students[0].eth_addresses, ["0x" + "1" * 40])
        self.assertEqual(students[0].group, "G1")

    def test_duplicate_student_id_is_rejected(self):
        client = FakeClient(
            {
                "COURSE_STUDENTS": [
                    {"Name": "Ada", "ID": "101"},
                    {"Name": "Grace", "ID": "101"},
                ]
            }
        )

        with self.assertRaisesRegex(ValueError, "duplicate ID"):
            read_students_from_google_sheet(client, "sheet-id", "COURSE_STUDENTS")

    def test_reads_ethernaut_rules_from_protected_sheet(self):
        address = "0x" + "a" * 40
        client = FakeClient(
            {
                "ETHERNAUT_LEVELS": [
                    {"Level": "Fallback", "Address": address, "Complexity": "4"},
                    {"Level": "Coin Flip", "Address": "0x" + "b" * 40, "Complexity": 6},
                ]
            }
        )

        complexity, mapping = read_ethernaut_config_from_google_sheet(
            client, "sheet-id", "ETHERNAUT_LEVELS"
        )

        self.assertEqual(complexity, {"Fallback": 4, "Coin Flip": 6})
        self.assertEqual(mapping[address], "Fallback")

    def test_reads_assignment1_settings_from_protected_sheet(self):
        professor_nft = "0x" + "a" * 40
        professor_wallet = "0x" + "b" * 40
        special_contract = "0x" + "c" * 40
        client = FakeClient(
            {
                "ASSIGNMENT1_CONFIG": [
                    {
                        "Professor NFT Contract": professor_nft,
                        "Professor Return Address": professor_wallet,
                        "Special Contract": special_contract,
                        "Start Block": 123,
                        "End Block": 456,
                        "Require Approval": "TRUE",
                    }
                ]
            }
        )

        config = read_assignment1_config_from_google_sheet(
            client, "sheet-id", "ASSIGNMENT1_CONFIG"
        )

        self.assertEqual(config.professor_nft_contract, professor_nft)
        self.assertEqual(config.professor_return_address, professor_wallet)
        self.assertEqual(config.special_contract, special_contract)
        self.assertEqual(config.start_block, 123)
        self.assertEqual(config.end_block, 456)
        self.assertTrue(config.require_approval)

    def test_matches_new_assignment1_nft_flows_in_order(self):
        student = "0x" + "1" * 40
        professor_nft = "0x" + "a" * 40
        professor_wallet = "0x" + "b" * 40
        personal_nft = "0x" + "d" * 40
        special_contract = "0x" + "c" * 40
        zero = "0x" + "0" * 40
        config = Assignment1Config(
            professor_nft_contract=professor_nft,
            professor_return_address=professor_wallet,
            special_contract=special_contract,
        )
        transfers = [
            {
                "blockNumber": "10",
                "transactionIndex": "1",
                "contractAddress": professor_nft,
                "tokenID": "7",
                "from": professor_wallet,
                "to": student,
                "hash": "0xreceive",
            },
            {
                "blockNumber": "11",
                "transactionIndex": "1",
                "contractAddress": professor_nft,
                "tokenID": "7",
                "from": student,
                "to": professor_wallet,
                "hash": "0xreturn",
            },
            {
                "blockNumber": "12",
                "transactionIndex": "1",
                "contractAddress": personal_nft,
                "tokenID": "42",
                "from": zero,
                "to": student,
                "hash": "0xmint",
            },
            {
                "blockNumber": "14",
                "transactionIndex": "1",
                "contractAddress": personal_nft,
                "tokenID": "42",
                "from": student,
                "to": special_contract,
                "hash": "0xspecial",
            },
        ]

        evidence = evaluate_assignment1_transfers(transfers, [student], config)

        self.assertEqual(evidence["professor_receive"]["hash"], "0xreceive")
        self.assertEqual(evidence["professor_return"]["hash"], "0xreturn")
        self.assertEqual(evidence["personal_mint"]["hash"], "0xmint")
        self.assertEqual(evidence["transfer_to_special"]["hash"], "0xspecial")

    def test_finds_token_specific_approval(self):
        class HexValue:
            def __init__(self, value):
                self.value = value

            def hex(self):
                return self.value

        w3 = MagicMock()
        w3.keccak.side_effect = [HexValue("0xapproval"), HexValue("0xapprovalall")]
        w3.eth.get_logs.return_value = [
            {"transactionHash": HexValue("0xapprovaltx")}
        ]

        tx_hash = find_erc721_approval(
            w3=w3,
            nft_contract="0x" + "d" * 40,
            owner="0x" + "1" * 40,
            approved_contract="0x" + "c" * 40,
            token_id="42",
            start_block=100,
            end_block=200,
        )

        self.assertEqual(tx_hash, "0xapprovaltx")
        topics = w3.eth.get_logs.call_args.args[0]["topics"]
        self.assertTrue(topics[3].endswith("2a"))

    def test_ethernaut_pass_requires_complexity_ten(self):
        wallet = "0x" + "1" * 40
        student = Student("Ada", "101", "", [wallet])
        result = check_ethernaut(
            student=student,
            completed_by_wallet={
                wallet: {
                    "count": 2,
                    "level_addresses": {"0x" + "a" * 40, "0x" + "b" * 40},
                    "level_names": {"Fallback", "Coin Flip"},
                }
            },
            level_complexity={"Fallback": 4, "Coin Flip": A2_PASS_COMPLEXITY - 4},
            level_addr_to_name={
                "0x" + "a" * 40: "Fallback",
                "0x" + "b" * 40: "Coin Flip",
            },
            repo_texts_cache={},
            gh=GitHubHelper(),
        )

        self.assertEqual(result.onchain_complexity, A2_PASS_COMPLEXITY)
        self.assertEqual(result.status, "PASS")

    def test_partial_evidence_goes_to_manual_review(self):
        status, reason = overall_status(
            "101",
            "all",
            Assignment1Result(status="PARTIAL"),
            EthernautResult(status="PASS"),
            [],
        )

        self.assertEqual(status, "REVIEW")
        self.assertIn("instructor review", reason)

    def test_result_writer_updates_current_worksheets_and_appends_history(self):
        client = FakeOutputClient()
        student = Student("Ada", "101", "https://github.com/ada", ["0x" + "1" * 40])
        submission = SubmissionResult(
            status="VALID", repository="ada/course", commit_sha="a" * 40
        )
        outcomes = {
            "101": {
                "assignment1": WorkOutcome(
                    work_id="assignment1",
                    report_status="SUBMITTED",
                    auto_status="PASS",
                    final_status="PASS",
                    network="sepolia",
                    commit_sha="a" * 40,
                )
            }
        }

        title, url = write_google_results(
            client=client,
            results_spreadsheet_id="result-sheet-id",
            students=[student],
            submissions={"101": submission},
            outcomes=outcomes,
            selected=("assignment1",),
            errors=[],
            run_mode="final",
            scope="assignment1",
        )

        self.assertTrue(title.startswith("FINAL_AUTOTEST_"))
        self.assertEqual(client.opened, "result-sheet-id")
        self.assertEqual(
            {worksheet.title for worksheet in client.spreadsheet.worksheets},
            {
                "Lab summary",
                "Assignment summary",
                "Autotest details",
                "Manual review",
                "Errors",
                "Run history",
            },
        )
        self.assertEqual(url, "https://docs.google.com/spreadsheets/d/result-sheet-id")
        for sheet_name in ("Lab summary", "Assignment summary", "Autotest details"):
            worksheet = client.spreadsheet.worksheet(sheet_name)
            self.assertEqual(len(worksheet.values[0]), len(worksheet.values[1]))
        history = client.spreadsheet.worksheet("Run history").values
        self.assertEqual(history[0][0], "Run UTC")
        self.assertEqual(history[1][1:4], ["FINAL", "assignment1", 1])
        self.assertEqual(history[1][4:7], [1, 1, 1])

        failed_outcomes = {
            "101": {
                "assignment1": WorkOutcome(
                    work_id="assignment1",
                    report_status="SUBMITTED",
                    auto_status="FAIL",
                    final_status="FAIL",
                    network="sepolia",
                    commit_sha="b" * 40,
                )
            }
        }
        write_google_results(
            client=client,
            results_spreadsheet_id="result-sheet-id",
            students=[student],
            submissions={"101": submission},
            outcomes=failed_outcomes,
            selected=("assignment1",),
            errors=[],
            run_mode="preview",
            scope="assignment1",
        )

        self.assertEqual(len(client.spreadsheet.worksheets), 6)
        history = client.spreadsheet.worksheet("Run history").values
        self.assertEqual(len(history), 3)
        self.assertEqual(history[2][1:4], ["PREVIEW", "assignment1", 1])
        self.assertEqual(history[2][8], 1)


if __name__ == "__main__":
    unittest.main()
