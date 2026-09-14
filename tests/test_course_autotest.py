from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from gspread.exceptions import WorksheetNotFound
from web3 import Web3

from scripts.course_autotest import (
    A2_PASS_COMPLEXITY,
    Assignment1Config,
    Assignment1Result,
    EthernautResult,
    GitHubHelper,
    Lab7Config,
    LabRequirementsConfig,
    SubmissionResult,
    SubscanClient,
    Student,
    TonCenterClient,
    WorkOutcome,
    WorkSubmission,
    WorkValidationResult,
    build_work_outcomes,
    check_ethernaut,
    evaluate_assignment1_transfers,
    find_erc721_approval,
    fetch_student_submission,
    overall_status,
    parse_submission_document,
    read_assignment1_config_from_google_sheet,
    read_ethernaut_config_from_google_sheet,
    read_lab7_config_from_google_sheet,
    read_lab_requirements_from_google_sheet,
    read_students_from_google_sheet,
    selected_work_ids,
    validate_lab1,
    validate_lab2_precheck,
    validate_lab3_precheck,
    validate_lab4,
    validate_lab5,
    validate_lab7,
    validate_lab8,
    validate_lab9,
    validate_lab10,
    validate_lab11,
    validate_lab12,
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

    def test_legacy_solution_report_gets_actionable_schema_error(self):
        import json

        document = {
            "student": {"student_id": "TEST-001"},
            "wallets": {"ethereum_sepolia": "0x" + "1" * 40},
            "labs": {},
        }

        with self.assertRaisesRegex(ValueError, "legacy submission format"):
            parse_submission_document(
                json.dumps(document), expected_student_id="TEST-001"
            )

    def test_scopes_keep_all_twelve_labs_and_four_assignments(self):
        self.assertEqual(len(selected_work_ids("labs")), 12)
        self.assertEqual(len(selected_work_ids("assignments")), 4)
        self.assertEqual(len(selected_work_ids("all")), 16)
        self.assertEqual(selected_work_ids("lab7"), ("lab7",))

    def test_lab1_passes_only_for_registered_sepolia_transfer(self):
        wallet = "0x" + "1" * 40
        recipient = "0x" + "2" * 40
        tx_hash = "0x" + "a" * 64
        student = Student("Ada", "101", "", [wallet])
        work = WorkSubmission(
            status="submitted",
            network="sepolia",
            evidence={
                "tx_hashes": [tx_hash],
                "recipient": recipient,
                "amount_eth": "0.0001",
            },
        )
        w3 = MagicMock()
        w3.eth.chain_id = 11155111
        w3.eth.get_transaction.return_value = {
            "from": wallet,
            "to": recipient,
            "value": 100_000_000_000_000,
        }
        w3.eth.get_transaction_receipt.return_value = {"status": 1}

        result = validate_lab1(student, work, w3, recipient)

        self.assertEqual(result.status, "PASS")
        self.assertIn(tx_hash, result.note)

        w3.eth.get_transaction.return_value["from"] = "0x" + "3" * 40
        result = validate_lab1(student, work, w3, recipient)
        self.assertEqual(result.status, "FAIL")
        self.assertIn("registered", result.note)

    def test_lab1_known_transaction_without_receipt_is_provider_error(self):
        wallet = "0x" + "1" * 40
        tx_hash = "0x" + "a" * 64
        work = WorkSubmission(
            status="submitted",
            network="sepolia",
            evidence={
                "tx_hashes": [tx_hash],
                "recipient": "0x" + "2" * 40,
                "amount_eth": "0.0001",
            },
        )
        w3 = MagicMock()
        w3.eth.chain_id = 11155111
        w3.eth.get_transaction.return_value = {
            "from": wallet,
            "to": "0x" + "2" * 40,
            "value": 100_000_000_000_000,
        }
        w3.eth.get_transaction_receipt.return_value = None

        result = validate_lab1(
            Student("Ada", "101", "", [wallet]), work, w3, "0x" + "2" * 40
        )

        self.assertEqual(result.status, "ERROR")
        self.assertIn("receipt is temporarily unavailable", result.note)

    def test_lab4_cross_checks_gas_and_fee(self):
        wallet = "0x" + "1" * 40
        tx_hash = "0x" + "b" * 64
        student = Student("Ada", "101", "", [wallet])
        work = WorkSubmission(
            status="submitted",
            network="sepolia",
            evidence={
                "tx_hashes": [tx_hash],
                "gas_limit": "21000",
                "gas_used": 21000,
                "transaction_fee_eth": "0.000021",
            },
            answers={
                "gas_limit_vs_gas_used": (
                    "Gas limit is the maximum while gas used is the actual amount."
                )
            },
        )
        w3 = MagicMock()
        w3.eth.chain_id = 11155111
        w3.eth.get_transaction.return_value = {
            "from": wallet,
            "gas": 21000,
            "gasPrice": 1_000_000_000,
        }
        w3.eth.get_transaction_receipt.return_value = {
            "status": 1,
            "gasUsed": 21000,
            "effectiveGasPrice": 1_000_000_000,
        }

        result = validate_lab4(student, work, w3)

        self.assertEqual(result.status, "PASS")
        self.assertIn("fee_wei=21000000000000", result.note)

    def test_lab5_requires_erc20_events_and_batch_transfer(self):
        wallet = "0x" + "1" * 40
        token = "0x" + "a" * 40
        transfer_txs = ["0x" + character * 64 for character in ("1", "2", "3")]
        disperse_tx = "0x" + "4" * 64
        student = Student("Ada", "101", "", [wallet])
        work = WorkSubmission(
            status="submitted",
            network="sepolia",
            evidence={
                "token_contract": token,
                "transfer_txs": transfer_txs,
                "disperse_tx": disperse_tx,
            },
        )
        transfer_topic = Web3.keccak(
            text="Transfer(address,address,uint256)"
        )
        wallet_topic = bytes.fromhex("0" * 24 + wallet[2:])
        recipient_topics = [
            bytes.fromhex("0" * 24 + character * 40)
            for character in ("2", "3", "4")
        ]

        def receipt(tx_hash):
            if tx_hash == disperse_tx:
                logs = [
                    {
                        "address": token,
                        "topics": [transfer_topic, wallet_topic, recipient_topic],
                    }
                    for recipient_topic in recipient_topics
                ]
            else:
                recipient_topic = recipient_topics[transfer_txs.index(tx_hash)]
                logs = [
                    {
                        "address": token,
                        "topics": [transfer_topic, wallet_topic, recipient_topic],
                    }
                ]
            return {"status": 1, "logs": logs}

        w3 = MagicMock()
        w3.eth.chain_id = 11155111
        w3.eth.get_code.return_value = b"\x60\x00"
        w3.eth.call.return_value = b"\x01"
        w3.eth.get_transaction.side_effect = lambda _tx_hash: {"from": wallet}
        w3.eth.get_transaction_receipt.side_effect = receipt

        result = validate_lab5(student, work, w3)

        self.assertEqual(result.status, "PASS")
        self.assertIn("3 Disperse Transfer events", result.note)

    def test_lab7_checks_class_dex_swaps_before_manual_valuation_review(self):
        wallet = "0x" + "1" * 40
        dex_alpha = "0x" + "a" * 40
        dex_beta = "0x" + "b" * 40
        tx_hash = "0x" + "7" * 64
        student = Student("Ada", "101", "", [wallet])
        work = WorkSubmission(
            status="submitted",
            network="sepolia",
            evidence={
                "dex_contracts": [dex_alpha, dex_beta],
                "swap_txs": [tx_hash],
                "initial_reserves": {
                    "alpha": {"TEST": "100", "USDC": "200"},
                    "beta": {"TEST": "150", "USDC": "180"},
                },
                "final_portfolio_value": "42.5",
            },
            answers={
                "strategy": (
                    "Buy on the cheaper class DEX and sell on the other after "
                    "checking fees and reserve changes."
                )
            },
        )
        w3 = MagicMock()
        w3.eth.chain_id = 11155111
        w3.eth.get_transaction.return_value = {"from": wallet, "to": dex_alpha}
        w3.eth.get_transaction_receipt.return_value = {
            "status": 1,
            "logs": [{"address": dex_alpha, "topics": []}],
        }

        result = validate_lab7(
            student, work, w3, Lab7Config(dex_alpha=dex_alpha, dex_beta=dex_beta)
        )

        self.assertEqual(result.status, "REVIEW")
        self.assertIn("successful class-DEX swap", result.note)

    def test_lab8_validates_westend_transfer_with_subscan(self):
        extrinsic_hash = "0x" + "8" * 64
        student = Student(
            "Ada", "101", "", [], polkadot_address="5RegisteredPolkadotAddress"
        )
        work = WorkSubmission(
            status="submitted",
            network="westend",
            evidence={
                "extrinsic_hashes": [extrinsic_hash],
                "recipient": "5RecipientPolkadotAddress",
                "amount": "1.25",
            },
        )
        subscan = MagicMock()
        subscan.get_extrinsic.return_value = {
            "success": True,
            "account_id": student.polkadot_address,
            "block_num": 123,
            "call_module": "Balances",
            "call_module_function": "transfer_keep_alive",
            "transfer": {
                "success": True,
                "to": "5RecipientPolkadotAddress",
                "amount": "1250000000000",
            },
        }

        result = validate_lab8(student, work, subscan)

        self.assertEqual(result.status, "PASS")
        subscan.get_extrinsic.assert_called_once_with("westend", extrinsic_hash)

    def test_subscan_client_uses_network_endpoint_and_api_key(self):
        extrinsic_hash = "0x" + "8" * 64
        response = MagicMock()
        response.json.return_value = {"code": 0, "data": {"success": True}}
        session = MagicMock()
        session.post.return_value = response

        result = SubscanClient("subscan-key", session).get_extrinsic(
            "westend", extrinsic_hash
        )

        self.assertEqual(result, {"success": True})
        session.post.assert_called_once_with(
            "https://westend.api.subscan.io/api/scan/extrinsic",
            headers={
                "Content-Type": "application/json",
                "User-Agent": "newuuz-course-checker",
                "X-API-Key": "subscan-key",
            },
            json={"hash": extrinsic_hash, "hide_events": False, "events_limit": 100},
            timeout=30,
        )

    def test_subscan_client_requires_api_key(self):
        with self.assertRaisesRegex(RuntimeError, "SUBSCAN_API_KEY"):
            SubscanClient("", MagicMock()).get_extrinsic(
                "westend", "0x" + "8" * 64
            )

    def test_lab9_validates_registered_xcm_extrinsic(self):
        extrinsic_hash = "0x" + "9" * 64
        student = Student(
            "Ada", "101", "", [], polkadot_address="5RegisteredPolkadotAddress"
        )
        work = WorkSubmission(
            status="submitted",
            network="westend",
            evidence={
                "source_chain": "Westend",
                "destination_chain": "Asset Hub Westend",
                "xcm_extrinsic_hashes": [extrinsic_hash],
            },
            answers={
                "xcm_execution_explanation": (
                    "The source chain sends an XCM message and Asset Hub executes "
                    "the corresponding reserve transfer instruction."
                )
            },
        )
        subscan = MagicMock()
        subscan.get_extrinsic.return_value = {
            "success": True,
            "account_id": student.polkadot_address,
            "block_num": 456,
            "call_module": "PolkadotXcm",
            "call_module_function": "limited_reserve_transfer_assets",
            "params": [],
            "event": [{"module_id": "XcmPallet", "event_id": "Sent"}],
        }

        result = validate_lab9(
            student, work, subscan, "Westend", "Asset Hub Westend"
        )

        self.assertEqual(result.status, "PASS")
        self.assertIn("XCM extrinsic", result.note)

    def test_lab10_validates_exact_ton_testnet_transfer(self):
        wallet = "0:" + "1" * 64
        recipient = "0:" + "2" * 64
        tx_hash = "a" * 64
        student = Student("Ada", "101", "", [], ton_address=wallet)
        work = WorkSubmission(
            status="submitted",
            network="TON testnet",
            evidence={
                "tx_hashes": [tx_hash],
                "recipient": recipient,
                "amount_ton": "0.01",
            },
        )
        toncenter = MagicMock()
        toncenter.addresses_equal.side_effect = (
            lambda left, right: str(left).lower() == str(right).lower()
        )
        toncenter.transactions.return_value = [
            {
                "account": wallet,
                "description": {"aborted": False},
                "out_msgs": [{"destination": recipient, "value": 9_933_333}],
            }
        ]

        result = validate_lab10(student, work, toncenter, recipient)

        self.assertEqual(result.status, "PASS")
        self.assertIn("received=0.009933333 TON", result.note)

    def test_toncenter_client_normalizes_user_friendly_address(self):
        friendly = "E" + "A" * 47
        response = MagicMock()
        response.json.return_value = {
            "ok": True,
            "result": "0:" + "A" * 64,
        }
        session = MagicMock()
        session.get.return_value = response

        result = TonCenterClient("ton-key", session).canonical_address(friendly)

        self.assertEqual(result, "0:" + "a" * 64)
        session.get.assert_called_once_with(
            "https://testnet.toncenter.com/api/v2/unpackAddress",
            params={"address": friendly},
            headers={
                "Accept": "application/json",
                "User-Agent": "newuuz-course-checker",
                "X-API-Key": "ton-key",
            },
            timeout=30,
        )

    def test_lab11_validates_jetton_wallets_and_trace(self):
        wallet = "0:" + "1" * 64
        master = "0:" + "2" * 64
        sender_wallet = "0:" + "3" * 64
        recipient_wallet = "0:" + "4" * 64
        tx_hash = "8dcf2bad906389160556e7dccca54497cd1b8ca5b609456093c26384b83c2d56"
        student = Student("Ada", "101", "", [], ton_address=wallet)
        work = WorkSubmission(
            status="submitted",
            network="TON testnet",
            evidence={
                "tx_hashes": [tx_hash],
                "jetton_master": master,
                "sender_jetton_wallet": sender_wallet,
                "recipient_jetton_wallet": recipient_wallet,
            },
            answers={
                "jetton_architecture_explanation": (
                    "The master controls jetton metadata while each holder has a "
                    "separate wallet contract that participates in transfers."
                )
            },
        )
        toncenter = MagicMock()
        toncenter.addresses_equal.side_effect = (
            lambda left, right: str(left).lower() == str(right).lower()
        )
        toncenter.jetton_transfers.return_value = [
            {
                "transaction_hash": "jc8rrZBjiRYFVufczKVEl80bjKW2CUVgk8JjhLg8LVY=",
                "transaction_aborted": False,
                "source": wallet,
                "source_wallet": sender_wallet,
                "jetton_master": master,
            }
        ]
        toncenter.traces.return_value = [{"messages": [{"destination": recipient_wallet}]}]

        result = validate_lab11(student, work, toncenter, master)

        self.assertEqual(result.status, "PASS")
        self.assertIn("jetton transfer", result.note)

    def test_lab12_validates_stonfi_swap_and_pinned_script(self):
        wallet = "0:" + "1" * 64
        router = "0:" + "2" * 64
        tx_hash = "c" * 64
        student = Student("Ada", "101", "", [], ton_address=wallet)
        work = WorkSubmission(
            status="submitted",
            network="TON testnet",
            evidence={
                "mode": "stonfi_swap",
                "tx_hashes": [tx_hash],
                "router_address": router,
            },
            links=["https://github.com/ada/course/blob/main/labs/lab12.ts"],
        )
        submission = SubmissionResult(
            status="VALID", repository="ada/course", commit_sha="d" * 40
        )
        github = MagicMock()
        github.get_repo_tree.return_value = [
            {"type": "blob", "path": "labs/lab12.ts"}
        ]
        toncenter = MagicMock()
        toncenter.addresses_equal.side_effect = (
            lambda left, right: str(left).lower() == str(right).lower()
        )
        toncenter.actions.return_value = [
            {
                "type": "JettonSwap",
                "success": True,
                "details": {"protocol": "STON.fi"},
                "accounts": [wallet, router],
            }
        ]

        result = validate_lab12(
            student, work, submission, github, toncenter, "stonfi_swap", router
        )

        self.assertEqual(result.status, "PASS")
        github.get_repo_tree.assert_called_once_with("ada", "course", "d" * 40)

    def test_lab12_hackton_requires_manual_confirmation(self):
        wallet = "0:" + "1" * 64
        student = Student("Ada", "101", "", [], ton_address=wallet)
        work = WorkSubmission(
            status="submitted",
            network="TON testnet",
            evidence={"mode": "hackton", "proof": "challenge proof"},
            answers={
                "security_explanation": (
                    "The exploit abuses a broken authorization boundary and the "
                    "submitted trace shows the resulting unauthorized state change."
                )
            },
        )

        result = validate_lab12(
            student,
            work,
            SubmissionResult(),
            MagicMock(),
            MagicMock(),
            "hackton",
            "",
        )

        self.assertEqual(result.status, "REVIEW")

    def test_lab2_precheck_never_executes_student_code(self):
        work = WorkSubmission(
            status="submitted",
            network="offchain",
            evidence={
                "input_1": "alpha",
                "input_2": "beta",
                "hash_1": 42,
                "hash_2": 42,
            },
            links=["https://github.com/ada/course/blob/main/lab2.py"],
            answers={
                "sha256_collision_explanation": (
                    "A weak hash has a tiny output space, while SHA-256 makes a "
                    "collision computationally infeasible."
                )
            },
        )
        submission = SubmissionResult(
            status="VALID", repository="ada/course", commit_sha="a" * 40
        )
        github = MagicMock()
        github.get_repo_tree.return_value = [
            {"type": "blob", "path": "labs/lab2.py"}
        ]

        result = validate_lab2_precheck(work, submission, github)

        self.assertEqual(result.status, "REVIEW")
        github.get_repo_tree.assert_called_once_with("ada", "course", "a" * 40)

    def test_lab3_precheck_rejects_hash_below_difficulty(self):
        work = WorkSubmission(
            status="submitted",
            network="offchain",
            evidence={
                "transactions": ["one", "two"],
                "merkle_root": "a" * 64,
                "difficulty": 4,
                "nonce": 10,
                "block_hash": "000f" + "b" * 60,
            },
            links=["https://github.com/ada/course/blob/main/lab3.py"],
        )
        submission = SubmissionResult(
            status="VALID", repository="ada/course", commit_sha="b" * 40
        )
        github = MagicMock()
        github.get_repo_tree.return_value = [
            {"type": "blob", "path": "labs/lab3.py"}
        ]

        result = validate_lab3_precheck(work, submission, github)

        self.assertEqual(result.status, "FAIL")
        self.assertIn("does not satisfy", result.note)

    def test_dedicated_validator_result_is_used_in_work_outcome(self):
        student = Student(
            "Ada", "101", "https://github.com/ada/course", ["0x" + "1" * 40]
        )
        submission = SubmissionResult(
            status="VALID",
            repository="ada/course",
            commit_sha="a" * 40,
            works={"lab1": WorkSubmission(status="submitted", network="sepolia")},
        )

        outcome = build_work_outcomes(
            students=[student],
            selected=("lab1",),
            submissions={"101": submission},
            a1_results={},
            a2_results={},
            validator_results={
                "101": {"lab1": WorkValidationResult("PASS", "on-chain proof")}
            },
        )["101"]["lab1"]

        self.assertEqual(outcome.auto_status, "PASS")
        self.assertEqual(outcome.final_status, "PASS")
        self.assertIn("on-chain proof", outcome.note)

    def test_lab6_reuses_nft_quest_onchain_result(self):
        student = Student(
            "Ada", "101", "https://github.com/ada/course", ["0x" + "1" * 40]
        )
        submission = SubmissionResult(
            status="VALID",
            repository="ada/course",
            commit_sha="a" * 40,
            works={"lab6": WorkSubmission(status="submitted", network="sepolia")},
        )

        outcome = build_work_outcomes(
            students=[student],
            selected=("lab6",),
            submissions={"101": submission},
            a1_results={"101": Assignment1Result(status="PASS", note="NFT flow")},
            a2_results={},
        )["101"]["lab6"]

        self.assertEqual(outcome.auto_status, "PASS")
        self.assertEqual(outcome.final_status, "PASS")
        self.assertIn("NFT flow", outcome.note)

    def test_unimplemented_assignment_is_reviewed_but_assignment1_can_pass(self):
        student = Student(
            "Ada", "101", "https://github.com/ada/course", ["0x" + "1" * 40]
        )
        submission = SubmissionResult(
            status="VALID",
            repository="ada/course",
            commit_sha="a" * 40,
            works={
                "assignment3": WorkSubmission(
                    status="submitted", network="sepolia"
                ),
                "assignment1": WorkSubmission(
                    status="submitted", network="sepolia"
                ),
            },
        )

        outcomes = build_work_outcomes(
            students=[student],
            selected=("assignment3", "assignment1"),
            submissions={"101": submission},
            a1_results={"101": Assignment1Result(status="PASS")},
            a2_results={},
        )["101"]

        self.assertEqual(outcomes["assignment3"].final_status, "REVIEW")
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

    def test_reads_lab7_class_dexes_from_protected_sheet(self):
        dex_alpha = "0x" + "a" * 40
        dex_beta = "0x" + "b" * 40
        client = FakeClient(
            {"LAB7_CONFIG": [{"DEX Alpha": dex_alpha, "DEX Beta": dex_beta}]}
        )

        config = read_lab7_config_from_google_sheet(
            client, "sheet-id", "LAB7_CONFIG"
        )

        self.assertEqual(config, Lab7Config(dex_alpha=dex_alpha, dex_beta=dex_beta))

    def test_reads_instructor_controlled_lab_requirements(self):
        eth_recipient = "0x" + "a" * 40
        ton_recipient = "E" + "A" * 47
        jetton_master = "E" + "B" * 47
        router = "E" + "C" * 47
        client = FakeClient(
            {
                "LAB_REQUIREMENTS": [
                    {
                        "Lab 1 Recipient": eth_recipient,
                        "Lab 9 Source Chain": "Westend",
                        "Lab 9 Destination Chain": "Asset Hub Westend",
                        "Lab 10 Recipient": ton_recipient,
                        "Lab 11 Jetton Master": jetton_master,
                        "Lab 12 Mode": "stonfi-swap",
                        "Lab 12 STON.fi Router": router,
                    }
                ]
            }
        )

        config = read_lab_requirements_from_google_sheet(
            client, "sheet-id", "LAB_REQUIREMENTS"
        )

        self.assertEqual(
            config,
            LabRequirementsConfig(
                lab1_recipient=eth_recipient,
                lab9_source_chain="Westend",
                lab9_destination_chain="Asset Hub Westend",
                lab10_recipient=ton_recipient,
                lab11_jetton_master=jetton_master,
                lab12_mode="stonfi_swap",
                lab12_stonfi_router=router,
            ),
        )

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
