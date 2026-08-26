from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from scripts.course_autotest import (
    A2_PASS_COMPLEXITY,
    Assignment1Config,
    Assignment1Result,
    EthernautResult,
    GitHubHelper,
    Student,
    check_ethernaut,
    evaluate_assignment1_transfers,
    find_erc721_approval,
    overall_status,
    read_assignment1_config_from_google_sheet,
    read_ethernaut_config_from_google_sheet,
    read_students_from_google_sheet,
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


class FakeOutputSpreadsheet:
    def __init__(self):
        self.id = "result-sheet-id"
        self.sheet1 = FakeOutputWorksheet("Sheet1", 1)
        self.worksheets = [self.sheet1]
        self.shared = []

    def share(self, email, perm_type, role, notify):
        self.shared.append(email)

    def add_worksheet(self, title, rows, cols):
        worksheet = FakeOutputWorksheet(title, len(self.worksheets) + 1)
        self.worksheets.append(worksheet)
        return worksheet

    def batch_update(self, body):
        pass


class FakeOutputClient:
    def __init__(self):
        self.created = None
        self.spreadsheet = FakeOutputSpreadsheet()

    def create(self, title, folder_id=None):
        self.created = (title, folder_id)
        return self.spreadsheet


class CourseAutotestTests(unittest.TestCase):
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

    def test_result_writer_creates_four_new_worksheets(self):
        client = FakeOutputClient()
        student = Student("Ada", "101", "https://github.com/ada", ["0x" + "1" * 40])

        title, url = write_google_results(
            client=client,
            results_folder_id="folder-id",
            share_email="teacher@example.edu",
            students=[student],
            a1_results={
                "101": Assignment1Result(
                    status="PASS",
                    professor_received_ok=True,
                    professor_returned_ok=True,
                    personal_mint_ok=True,
                    approval_ok=True,
                    transfer_to_special_ok=True,
                )
            },
            a2_results={"101": EthernautResult(status="NOT RUN")},
            errors=[],
            run_mode="final",
            scope="assignment1",
        )

        self.assertTrue(title.startswith("FINAL_AUTOTEST_"))
        self.assertEqual(client.created[1], "folder-id")
        self.assertEqual(
            [worksheet.title for worksheet in client.spreadsheet.worksheets],
            ["Closed list", "Autotest details", "Manual review", "Errors"],
        )
        self.assertEqual(client.spreadsheet.shared, ["teacher@example.edu"])
        self.assertEqual(url, "https://docs.google.com/spreadsheets/d/result-sheet-id")
        for worksheet in client.spreadsheet.worksheets[:2]:
            self.assertEqual(len(worksheet.values[0]), len(worksheet.values[1]))


if __name__ == "__main__":
    unittest.main()
