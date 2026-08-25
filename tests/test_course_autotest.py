from __future__ import annotations

import unittest

from scripts.course_autotest import (
    A2_PASS_COMPLEXITY,
    Assignment1Result,
    EthernautResult,
    GitHubHelper,
    Student,
    check_ethernaut,
    overall_status,
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
                    status="PASS", token_ok=True, swap_ok=True, nft_ok=True
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


if __name__ == "__main__":
    unittest.main()
