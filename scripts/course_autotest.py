from __future__ import annotations

import argparse
import base64
import json
import math
import os
import re
import sys
import time
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import gspread
import requests
from google.oauth2.service_account import Credentials
from web3 import Web3

ETH_RE = re.compile(r"0x[a-fA-F0-9]{40}")
PROFILE_RE = re.compile(r"^https?://github\.com/([A-Za-z0-9_.-]+)/?$", re.IGNORECASE)
REPO_RE = re.compile(
    r"^https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)/?$",
    re.IGNORECASE,
)
OWNER_REPO_RE = re.compile(r"^([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)$")
TEXT_EXTS = {".md", ".txt", ".sol", ".js", ".ts", ".py", ".yaml", ".yml", ".toml"}
KEYWORDS_A1 = [
    "assignment1",
    "assignment-1",
    "blockchain",
    "erc20",
    "erc721",
    "token",
    "nft",
    "solidity",
    "newuu",
    "newuuz",
]
KEYWORDS_A2 = [
    "assignment2",
    "assignment-2",
    "ethernaut",
    "fallback",
    "fallout",
    "coinflip",
    "reentrancy",
    "puzzlewallet",
    "motorbike",
]
A1_DEFAULT_END_BLOCK = 99999999
A2_PASS_COMPLEXITY = 10
A2_BONUS_LEVELS = 15


@dataclass
class Student:
    name: str
    student_id: str
    github_raw: str
    eth_addresses: list[str]
    email: str = ""
    polkadot_address: str = ""
    ton_address: str = ""
    group: str = ""
    active: bool = True


@dataclass(frozen=True)
class Assignment1Config:
    professor_nft_contract: str
    professor_return_address: str
    special_contract: str
    start_block: int = 0
    end_block: int = A1_DEFAULT_END_BLOCK
    require_approval: bool = True


@dataclass
class Assignment1Result:
    status: str = "-"
    repo: str = ""
    github_ok: bool = False
    commits_ok: bool = False
    professor_received_ok: bool = False
    professor_returned_ok: bool = False
    personal_mint_ok: bool = False
    approval_ok: bool = False
    transfer_to_special_ok: bool = False
    approval_required: bool = True
    professor_nft_contract: str = ""
    professor_token_id: str = ""
    personal_nft_contract: str = ""
    personal_token_id: str = ""
    professor_receive_tx_hash: str = ""
    professor_return_tx_hash: str = ""
    personal_mint_tx_hash: str = ""
    approval_tx_hash: str = ""
    transfer_to_special_tx_hash: str = ""
    note: str = ""


@dataclass
class EthernautResult:
    status: str = "-"
    matched_wallet: str = ""
    onchain_unique_levels: int = 0
    onchain_total_submits: int = 0
    onchain_levels: list[str] = field(default_factory=list)
    onchain_complexity: int | None = None
    declared_levels: list[str] = field(default_factory=list)
    declared_complexity: int | None = None
    # Detailed A2 evidence. These are filled either from LevelCompletedLog
    # or from the Etherscan txlist fallback.
    submit_tx_hashes: list[str] = field(default_factory=list)
    submit_blocks: list[str] = field(default_factory=list)
    submitted_instances: list[str] = field(default_factory=list)
    raw_level_addresses: list[str] = field(default_factory=list)
    level_details: list[str] = field(default_factory=list)
    methods: list[str] = field(default_factory=list)
    bonus_15_levels: bool = False
    note: str = ""


class GitHubHelper:
    def __init__(self, token: str | None = None) -> None:
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/vnd.github+json",
                "User-Agent": "newuuz-course-checker",
            }
        )
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

    def _get(self, url: str, **kwargs) -> requests.Response:
        resp = self.session.get(url, timeout=30, **kwargs)
        resp.raise_for_status()
        return resp

    def get_repo(self, owner: str, repo: str) -> dict[str, Any]:
        return self._get(f"https://api.github.com/repos/{owner}/{repo}").json()

    def list_commits(
        self, owner: str, repo: str, per_page: int = 5
    ) -> list[dict[str, Any]]:
        return self._get(
            f"https://api.github.com/repos/{owner}/{repo}/commits",
            params={"per_page": per_page},
        ).json()

    def list_user_repos(
        self, username: str, per_page: int = 100
    ) -> list[dict[str, Any]]:
        return self._get(
            f"https://api.github.com/users/{username}/repos",
            params={"per_page": per_page, "sort": "updated"},
        ).json()

    def get_repo_tree(self, owner: str, repo: str, branch: str) -> list[dict[str, Any]]:
        data = self._get(
            f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}",
            params={"recursive": "1"},
        ).json()
        return data.get("tree", [])

    def get_content(
        self, owner: str, repo: str, path: str, ref: str | None = None
    ) -> str:
        data = self._get(
            f"https://api.github.com/repos/{owner}/{repo}/contents/{path}",
            params={"ref": ref} if ref else None,
        ).json()
        content = data.get("content", "")
        encoding = data.get("encoding")
        if encoding == "base64":
            return base64.b64decode(content).decode("utf-8", errors="ignore")
        download_url = data.get("download_url")
        if download_url:
            return self._get(download_url).text
        return ""


def normalize_address(value: str) -> str:
    return Web3.to_checksum_address(value)


def extract_addresses(text: str | None) -> list[str]:
    if not text:
        return []
    found = ETH_RE.findall(str(text))
    unique = []
    seen = set()
    for addr in found:
        low = addr.lower()
        if low not in seen:
            seen.add(low)
            unique.append(low)
    return unique


GOOGLE_SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def google_client(service_account_json: str) -> gspread.Client:
    """Create a Google client from a GitHub Actions secret."""
    if not service_account_json.strip():
        raise ValueError("GOOGLE_SERVICE_ACCOUNT_JSON is empty")
    info = json.loads(service_account_json)
    credentials = Credentials.from_service_account_info(info, scopes=GOOGLE_SCOPES)
    return gspread.authorize(credentials)


def normalize_header(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip()).lower()


def row_value(row: dict[str, Any], *aliases: str) -> str:
    normalized = {normalize_header(key): value for key, value in row.items()}
    for alias in aliases:
        value = normalized.get(normalize_header(alias))
        if value is not None:
            return str(value).strip()
    return ""


def normalize_student_id(value: str) -> str:
    return value[:-2] if re.fullmatch(r"\d+\.0", value) else value


def is_active_value(value: str) -> bool:
    return normalize_header(value) not in {"0", "false", "no", "inactive", "нет", "-"}


def env_int(name: str, default: int) -> int:
    value = os.getenv(name, "").strip()
    return int(value) if value else default


def read_students_from_google_sheet(
    client: gspread.Client,
    spreadsheet_id: str,
    worksheet_name: str,
) -> list[Student]:
    worksheet = client.open_by_key(spreadsheet_id).worksheet(worksheet_name)
    rows = worksheet.get_all_records(default_blank="")
    students: list[Student] = []
    seen_ids: set[str] = set()

    for row_number, row in enumerate(rows, start=2):
        active_raw = row_value(row, "Active", "Активен")
        if active_raw and not is_active_value(active_raw):
            continue
        name = row_value(row, "Name", "Full name", "ФИО")
        student_id = normalize_student_id(
            row_value(row, "ID", "Student ID", "ID студента")
        )
        if not name and not student_id:
            continue
        if not name or not student_id:
            raise ValueError(
                f"Worksheet '{worksheet_name}', row {row_number}: Name and ID are required"
            )
        if student_id in seen_ids:
            raise ValueError(
                f"Worksheet '{worksheet_name}', row {row_number}: duplicate ID '{student_id}'"
            )
        seen_ids.add(student_id)

        student = Student(
            name=name,
            student_id=student_id,
            email=row_value(row, "Email", "E-mail", "Почта"),
            github_raw=row_value(row, "GitHub", "Github", "Repository", "Репозиторий"),
            eth_addresses=extract_addresses(
                row_value(row, "Ethereum", "Ethereum address", "ETH address", "ETH")
            ),
            polkadot_address=row_value(row, "Polkadot", "Polkadot address"),
            ton_address=row_value(row, "TON", "TON address", "TON testnet"),
            group=row_value(row, "Group", "Группа"),
            active=True,
        )
        students.append(student)

    if not students:
        raise ValueError(f"No active students found in worksheet '{worksheet_name}'")
    return students


def read_ethernaut_config_from_google_sheet(
    client: gspread.Client,
    spreadsheet_id: str,
    worksheet_name: str,
) -> tuple[dict[str, int], dict[str, str]]:
    """Read teacher-maintained level names, addresses and complexity scores."""
    try:
        rows = (
            client.open_by_key(spreadsheet_id)
            .worksheet(worksheet_name)
            .get_all_records(default_blank="")
        )
    except gspread.WorksheetNotFound:
        return {}, {}

    complexity_by_name: dict[str, int] = {}
    address_to_name: dict[str, str] = {}
    for row in rows:
        name = row_value(row, "Level", "Name", "Level name")
        address = row_value(row, "Address", "Level address").lstrip("'")
        complexity_raw = row_value(row, "Complexity", "Score")
        if not name:
            continue
        try:
            complexity_by_name[name] = int(float(complexity_raw))
        except (TypeError, ValueError):
            continue
        if ETH_RE.fullmatch(address):
            address_to_name[address.lower()] = name
    return complexity_by_name, address_to_name


def read_assignment1_config_from_google_sheet(
    client: gspread.Client,
    spreadsheet_id: str,
    worksheet_name: str,
) -> Assignment1Config:
    """Read the instructor-controlled addresses for the current NFT Quest."""
    rows = (
        client.open_by_key(spreadsheet_id)
        .worksheet(worksheet_name)
        .get_all_records(default_blank="")
    )
    if not rows:
        raise ValueError(f"Worksheet '{worksheet_name}' must contain one config row")

    row = rows[0]

    def address(*names: str) -> str:
        value = row_value(row, *names).lstrip("'")
        if not ETH_RE.fullmatch(value):
            raise ValueError(
                f"Worksheet '{worksheet_name}': '{names[0]}' must be a valid 0x address"
            )
        return value.lower()

    def block_number(default: int, *names: str) -> int:
        value = row_value(row, *names)
        if not value:
            return default
        try:
            number = int(float(value))
        except (TypeError, ValueError) as exc:
            raise ValueError(
                f"Worksheet '{worksheet_name}': '{names[0]}' must be an integer"
            ) from exc
        if number < 0:
            raise ValueError(
                f"Worksheet '{worksheet_name}': '{names[0]}' cannot be negative"
            )
        return number

    start_block = block_number(0, "Start Block", "Start block")
    end_block = block_number(A1_DEFAULT_END_BLOCK, "End Block", "End block")
    if end_block < start_block:
        raise ValueError(
            f"Worksheet '{worksheet_name}': End Block cannot be smaller than Start Block"
        )

    approval_raw = row_value(row, "Require Approval", "Approval required")
    require_approval = is_active_value(approval_raw) if approval_raw else True

    return Assignment1Config(
        professor_nft_contract=address(
            "Professor NFT Contract", "Professor NFT", "Course NFT Contract"
        ),
        professor_return_address=address(
            "Professor Return Address", "Professor Wallet", "Return Address"
        ),
        special_contract=address("Special Contract", "NFT Receiver Contract"),
        start_block=start_block,
        end_block=end_block,
        require_approval=require_approval,
    )


def score_repo_candidate(repo: dict[str, Any]) -> int:
    text = " ".join(
        [
            str(repo.get("name", "")),
            str(repo.get("description", "")),
            str(repo.get("homepage", "")),
        ]
    ).lower()
    score = 0
    for kw in KEYWORDS_A1 + KEYWORDS_A2:
        if kw in text:
            score += 5
    if repo.get("language") in {"Solidity", "JavaScript", "TypeScript", "Python"}:
        score += 2
    if not repo.get("fork"):
        score += 1
    return score


def resolve_repo(github: str, gh: GitHubHelper) -> tuple[str, str, str]:
    github = (github or "").strip()
    if not github:
        raise ValueError("missing GitHub URL")

    m = REPO_RE.match(github)
    if m:
        return m.group(1), m.group(2), f"repo_from_url:{m.group(1)}/{m.group(2)}"

    m = OWNER_REPO_RE.match(github)
    if m:
        return m.group(1), m.group(2), f"repo_from_string:{m.group(1)}/{m.group(2)}"

    m = PROFILE_RE.match(github)
    if not m:
        raise ValueError("github field is neither profile nor repo URL")

    username = m.group(1)
    repos = gh.list_user_repos(username)
    if not repos:
        raise ValueError(f"no public repos for profile {username}")

    ranked = sorted(repos, key=score_repo_candidate, reverse=True)
    top = ranked[0]
    return username, top["name"], f"repo_from_profile:{username}/{top['name']}"


def collect_repo_texts(
    gh: GitHubHelper, owner: str, repo: str, default_branch: str
) -> dict[str, str]:
    tree = gh.get_repo_tree(owner, repo, default_branch)
    candidates: list[tuple[int, str]] = []
    for item in tree:
        if item.get("type") != "blob":
            continue
        path = item.get("path", "")
        ext = Path(path).suffix.lower()
        if ext not in TEXT_EXTS:
            continue
        path_low = path.lower()
        score = 0
        if any(
            keyword in path_low
            for keyword in [
                "readme",
                "assign",
                "ethernaut",
                "erc20",
                "erc721",
                "token",
                "nft",
            ]
        ):
            score += 10
        if ext in {".md", ".sol"}:
            score += 3
        candidates.append((score, path))

    candidates.sort(reverse=True)
    texts: dict[str, str] = {}
    for _, path in candidates[:25]:
        try:
            texts[path] = gh.get_content(owner, repo, path, ref=default_branch)
            time.sleep(0.1)
        except Exception:
            continue
    return texts


def fetch_sepolia_level_map(
    session: requests.Session, ordered_levels: list[str]
) -> dict[str, str]:
    url = "https://raw.githubusercontent.com/OpenZeppelin/ethernaut/master/deploy.sepolia.json"
    try:
        resp = session.get(url, timeout=20)
        resp.raise_for_status()
        data = resp.json()
        result: dict[str, str] = {}
        for i, level_name in enumerate(ordered_levels, start=1):
            value = data.get(str(i))
            if isinstance(value, str) and ETH_RE.fullmatch(value):
                result[value.lower()] = level_name
        return result
    except Exception:
        return {}


def build_web3(rpc_url: str) -> Web3:
    w3 = Web3(Web3.HTTPProvider(rpc_url, request_kwargs={"timeout": 30}))
    if not w3.is_connected():
        raise RuntimeError(f"Unable to connect to RPC endpoint: {rpc_url}")
    return w3


def get_ethernaut_logs(
    w3: Web3, ethernaut_address: str, start_block: int = 0, chunk_size: int = 100_000
) -> list[Any]:
    latest = w3.eth.block_number
    topic0 = w3.keccak(text="LevelCompletedLog(address,address)")
    contract = Web3.to_checksum_address(ethernaut_address)
    logs = []
    current = start_block
    total_chunks = max(1, math.ceil((latest - start_block + 1) / chunk_size))
    chunk_num = 0
    while current <= latest:
        end = min(current + chunk_size - 1, latest)
        chunk_num += 1
        try:
            chunk_logs = w3.eth.get_logs(
                {
                    "fromBlock": current,
                    "toBlock": end,
                    "address": contract,
                    "topics": [topic0],
                }
            )
            logs.extend(chunk_logs)
        except Exception:
            if chunk_size <= 5_000:
                raise
            chunk_size = max(chunk_size // 2, 5_000)
            print(
                f"[WARN] Ethernaut log range was rejected; retrying with {chunk_size}-block chunks"
            )
            continue
        current = end + 1
        if chunk_num % 10 == 0 or chunk_num == total_chunks:
            print(
                f"[INFO] Ethernaut logs chunk {chunk_num}/{total_chunks}, total logs: {len(logs)}"
            )
        time.sleep(0.05)
    return logs


def parse_completed_logs(
    logs: list[Any], level_addr_to_name: dict[str, str]
) -> dict[str, dict[str, Any]]:
    by_wallet: dict[str, dict[str, Any]] = defaultdict(
        lambda: {"count": 0, "level_addresses": set(), "level_names": set()}
    )
    for log in logs:
        topics = log["topics"]
        if len(topics) < 2:
            continue
        wallet = "0x" + topics[1].hex()[-40:]
        data_hex = (
            log["data"].hex() if hasattr(log["data"], "hex") else str(log["data"])
        )
        data_hex = data_hex[2:] if data_hex.startswith("0x") else data_hex
        if len(data_hex) >= 64:
            level_addr = "0x" + data_hex[-40:]
        else:
            level_addr = ""
        entry = by_wallet[wallet.lower()]
        entry["count"] += 1
        if level_addr:
            entry["level_addresses"].add(level_addr.lower())
            level_name = level_addr_to_name.get(level_addr.lower())
            if level_name:
                entry["level_names"].add(level_name)
    return by_wallet


def find_declared_levels_in_texts(
    texts: dict[str, str], known_levels: list[str]
) -> list[str]:
    found: list[str] = []
    joined = "\n".join(texts.values()).lower()
    for level in known_levels:
        variants = {
            level.lower(),
            level.lower().replace("two", "2"),
            level.lower().replace("one", "1"),
        }
        if any(v in joined for v in variants):
            found.append(level)
    seen = set()
    out = []
    for level in found:
        if level not in seen:
            seen.add(level)
            out.append(level)
    return out


ZERO_ADDR = "0x0000000000000000000000000000000000000000"
ETHERSCAN_V2_URL = "https://api.etherscan.io/v2/api"


def etherscan_v2_get(params: dict[str, Any], timeout: int = 20) -> dict[str, Any]:
    """Small wrapper for Etherscan V2 Sepolia API."""
    api_key = os.getenv("ETHERSCAN_API_KEY", "").strip()
    full_params = {"chainid": "11155111", **params, "apikey": api_key}
    resp = requests.get(ETHERSCAN_V2_URL, params=full_params, timeout=timeout)
    return resp.json()


def _method_input_address(input_hex: str, arg_index: int = 0) -> str:
    """Decode a static address argument from calldata by index.

    4 bytes selector + 32-byte slots. Address is last 20 bytes of the slot.
    """
    if (
        not input_hex
        or not isinstance(input_hex, str)
        or not input_hex.startswith("0x")
    ):
        return ""
    data = input_hex[10:]  # skip selector
    start = arg_index * 64
    slot = data[start : start + 64]
    if len(slot) != 64:
        return ""
    addr = "0x" + slot[-40:]
    return addr.lower() if Web3.is_address(addr) else ""


def fetch_ethernaut_tx_fallback(
    wallets: list[str],
    ethernaut_address: str,
    start_block: int = 0,
) -> dict[str, dict[str, Any]]:
    """Fallback A2 detector using Etherscan normal transactions.

    It does NOT replace real LevelCompletedLog parsing. It is a safety net for
    current Ethernaut UI/API cases where RPC log parsing or level mapping fails.
    It looks for actual transactions from a wallet to the Ethernaut game contract
    with functionName/method indicating submitLevelInstance.
    """
    out: dict[str, dict[str, Any]] = {}
    api_key = os.getenv("ETHERSCAN_API_KEY", "").strip()
    if not api_key:
        return out

    ethernaut_low = ethernaut_address.lower()
    for wallet in wallets:
        wallet_low = wallet.lower()
        try:
            data = etherscan_v2_get(
                {
                    "module": "account",
                    "action": "txlist",
                    "address": wallet_low,
                    "startblock": start_block,
                    "endblock": 99999999,
                    "page": 1,
                    "offset": 200,
                    "sort": "desc",
                }
            )
        except Exception as exc:
            raise RuntimeError(
                f"A2 Etherscan request failed for {wallet_low}: {exc}"
            ) from exc

        status = str(data.get("status", ""))
        message = str(data.get("message", ""))
        result = data.get("result", [])
        if status != "1":
            # Empty wallet is normal.
            if "No transactions found" not in message:
                raise RuntimeError(
                    f"A2 Etherscan response for {wallet_low}: {message} | {result}"
                )
            continue
        if not isinstance(result, list):
            continue

        submit_txs: list[str] = []
        submit_blocks: list[str] = []
        submit_methods: list[str] = []
        create_txs: list[str] = []
        other_ethernaut_txs: list[str] = []
        submitted_instances: set[str] = set()

        for tx in result:
            to_addr = str(tx.get("to", "")).lower()
            from_addr = str(tx.get("from", "")).lower()
            if from_addr != wallet_low or to_addr != ethernaut_low:
                continue
            if str(tx.get("isError", "0")) != "0":
                continue

            tx_hash = str(tx.get("hash", ""))
            function_name = str(tx.get("functionName", "")).lower()
            method_id = str(tx.get("methodId", "")).lower()
            input_hex = str(tx.get("input", ""))
            other_ethernaut_txs.append(tx_hash)

            # Etherscan methodName is usually "Submit Level Instance" or
            # functionName is "submitLevelInstance(address _instance)".
            is_submit = (
                ("submit" in function_name and "level" in function_name)
                or method_id
                in {
                    # Some explorers omit functionName; keep methodId fallback open.
                    # If selector changes, functionName will still catch it.
                }
            )
            is_create = "create" in function_name and "level" in function_name

            if is_submit:
                submit_txs.append(tx_hash)
                submit_blocks.append(str(tx.get("blockNumber", "")))
                method_label = (
                    str(tx.get("functionName", "")).strip()
                    or str(tx.get("methodId", "")).strip()
                    or "submitLevelInstance"
                )
                submit_methods.append(method_label)
                inst = _method_input_address(input_hex, 0)
                if inst:
                    submitted_instances.add(inst)
            elif is_create:
                create_txs.append(tx_hash)

        if submit_txs:
            out[wallet_low] = {
                "submit_count": len(submit_txs),
                "submit_txs": submit_txs,
                "submit_blocks": submit_blocks,
                "submit_methods": submit_methods,
                "create_txs": sorted(set(create_txs)),
                "submitted_instances": sorted(submitted_instances),
                "other_ethernaut_txs": sorted(set(other_ethernaut_txs)),
                "raw_level_addresses": [],
                "level_names": [],
                "level_details": [],
            }
        time.sleep(0.25)
    return out


def enrich_ethernaut_tx_fallback_with_receipts(
    w3: Web3,
    tx_fallback_by_wallet: dict[str, dict[str, Any]],
    ethernaut_address: str,
    level_addr_to_name: dict[str, str],
) -> None:
    """Add level addresses/names/details to Etherscan tx fallback using receipts.

    The normal txlist endpoint reliably tells us that a wallet called
    submitLevelInstance(instance). The receipt lets us read the emitted
    LevelCompletedLog(player, level) and therefore recover the real level
    address/name when the level map is available.
    """
    topic0 = w3.keccak(text="LevelCompletedLog(address,address)")
    ethernaut_low = ethernaut_address.lower()

    for wallet, info in tx_fallback_by_wallet.items():
        raw_level_addresses: set[str] = set()
        level_names: set[str] = set()
        level_details: list[str] = []
        submit_txs = info.get("submit_txs", []) or []

        for tx_hash in submit_txs:
            try:
                receipt = w3.eth.get_transaction_receipt(tx_hash)
            except Exception as exc:
                print(f"[WARN] A2 receipt fallback error {tx_hash}: {exc}")
                continue

            for log in receipt.get("logs", []):
                try:
                    if str(log.get("address", "")).lower() != ethernaut_low:
                        continue
                    topics = log.get("topics", [])
                    if not topics or topics[0] != topic0:
                        continue

                    # Player is indexed in topic[1]; level address is in data.
                    data_hex = (
                        log.get("data", b"").hex()
                        if hasattr(log.get("data", b""), "hex")
                        else str(log.get("data", ""))
                    )
                    if data_hex.startswith("0x"):
                        data_hex = data_hex[2:]
                    level_addr = (
                        "0x" + data_hex[-40:].lower() if len(data_hex) >= 64 else ""
                    )
                    if not level_addr:
                        continue

                    raw_level_addresses.add(level_addr)
                    level_name = level_addr_to_name.get(level_addr.lower(), "")
                    if level_name:
                        level_names.add(level_name)
                        level_details.append(f"{level_name} | {level_addr} | {tx_hash}")
                    else:
                        level_details.append(f"Unknown | {level_addr} | {tx_hash}")
                except Exception:
                    continue

        info["raw_level_addresses"] = sorted(raw_level_addresses)
        info["level_names"] = sorted(level_names)
        info["level_details"] = level_details


def _topic_addr(topic_hex: str) -> str:
    return "0x" + topic_hex[-40:].lower()


def _address_to_topic(address: str) -> str:
    return "0x" + address.lower().replace("0x", "").rjust(64, "0")


def fetch_nft_transfers_for_wallets(
    wallets: list[str], start_block: int, end_block: int
) -> list[dict[str, Any]]:
    """Load indexed ERC721 transfers for registered wallets from Etherscan."""
    api_key = os.getenv("ETHERSCAN_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "ETHERSCAN_API_KEY is required for the Assignment 1 NFT check"
        )

    transfers: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str, str, str]] = set()
    url = "https://api.etherscan.io/v2/api"
    for wallet in sorted({wallet.lower() for wallet in wallets if wallet}):
        params = {
            "chainid": "11155111",
            "module": "account",
            "action": "tokennfttx",
            "address": wallet,
            "startblock": start_block,
            "endblock": end_block,
            "sort": "asc",
            "apikey": api_key,
        }
        try:
            response = requests.get(url, params=params, timeout=20)
            response.raise_for_status()
            data = response.json()
        except Exception as exc:
            raise RuntimeError(
                f"A1 NFT Etherscan request failed for {wallet}: {exc}"
            ) from exc

        status = str(data.get("status", ""))
        message = str(data.get("message", ""))
        rows = data.get("result", [])
        if status != "1":
            if "No transactions found" not in message:
                raise RuntimeError(
                    f"A1 NFT Etherscan response for {wallet}: {message} | {rows}"
                )
            time.sleep(0.25)
            continue
        if not isinstance(rows, list):
            raise RuntimeError(f"A1 NFT Etherscan returned invalid rows for {wallet}")

        for raw in rows:
            item = dict(raw)
            for key in ("from", "to", "contractAddress"):
                item[key] = str(item.get(key, "")).lower()
            item["tokenID"] = str(item.get("tokenID", ""))
            item["hash"] = str(item.get("hash", ""))
            dedupe_key = (
                item["hash"],
                item["contractAddress"],
                item["tokenID"],
                item["from"],
                item["to"],
            )
            if dedupe_key not in seen:
                seen.add(dedupe_key)
                transfers.append(item)
        time.sleep(0.25)

    return sorted(transfers, key=_nft_transfer_order)


def _int_field(item: dict[str, Any], name: str) -> int:
    try:
        value = str(item.get(name, "0"))
        return int(value, 16 if value.lower().startswith("0x") else 10)
    except (TypeError, ValueError):
        return 0


def _nft_transfer_order(item: dict[str, Any]) -> tuple[int, int, int]:
    return (
        _int_field(item, "blockNumber"),
        _int_field(item, "transactionIndex"),
        _int_field(item, "logIndex"),
    )


def evaluate_assignment1_transfers(
    transfers: list[dict[str, Any]],
    wallets: list[str],
    config: Assignment1Config,
) -> dict[str, Any]:
    """Match the two required ERC721 flows while preserving transaction order."""
    wallet_set = {wallet.lower() for wallet in wallets if wallet}
    zero_address = "0x0000000000000000000000000000000000000000"
    ordered = sorted(transfers, key=_nft_transfer_order)

    professor_receives = [
        item
        for item in ordered
        if item.get("contractAddress") == config.professor_nft_contract
        and item.get("to") in wallet_set
    ]
    professor_receive = professor_receives[0] if professor_receives else None
    professor_return = None
    for received in professor_receives:
        received_order = _nft_transfer_order(received)
        received_wallet = received.get("to")
        for item in ordered:
            if (
                _nft_transfer_order(item) > received_order
                and item.get("contractAddress") == config.professor_nft_contract
                and item.get("tokenID") == received.get("tokenID")
                and item.get("from") == received_wallet
                and item.get("to") == config.professor_return_address
            ):
                professor_receive = received
                professor_return = item
                break
        if professor_return:
            break

    personal_mints = [
        item
        for item in ordered
        if item.get("from") == zero_address
        and item.get("to") in wallet_set
        and item.get("contractAddress") != config.professor_nft_contract
    ]
    personal_mint = personal_mints[0] if personal_mints else None
    transfer_to_special = None
    for minted in personal_mints:
        minted_order = _nft_transfer_order(minted)
        minted_wallet = minted.get("to")
        for item in ordered:
            if (
                _nft_transfer_order(item) > minted_order
                and item.get("contractAddress") == minted.get("contractAddress")
                and item.get("tokenID") == minted.get("tokenID")
                and item.get("from") == minted_wallet
                and item.get("to") == config.special_contract
            ):
                personal_mint = minted
                transfer_to_special = item
                break
        if transfer_to_special:
            break

    return {
        "professor_receive": professor_receive,
        "professor_return": professor_return,
        "personal_mint": personal_mint,
        "transfer_to_special": transfer_to_special,
    }


def find_erc721_approval(
    w3: Web3,
    nft_contract: str,
    owner: str,
    approved_contract: str,
    token_id: str,
    start_block: int,
    end_block: int,
) -> str:
    """Return a matching Approval/ApprovalForAll transaction hash, if present."""
    if end_block < start_block:
        return ""
    contract = Web3.to_checksum_address(nft_contract)
    owner_topic = _address_to_topic(owner)
    approved_topic = _address_to_topic(approved_contract)
    approval_topic = w3.keccak(
        text="Approval(address,address,uint256)"
    ).hex()
    approval_for_all_topic = w3.keccak(
        text="ApprovalForAll(address,address,bool)"
    ).hex()
    try:
        token_number = int(
            token_id, 16 if token_id.lower().startswith("0x") else 10
        )
        token_topic = "0x" + hex(token_number)[2:].rjust(64, "0")
    except ValueError:
        return ""

    queries = [
        [approval_topic, owner_topic, approved_topic, token_topic],
        [approval_for_all_topic, owner_topic, approved_topic],
    ]
    for topics in queries:
        logs = w3.eth.get_logs(
            {
                "address": contract,
                "fromBlock": start_block,
                "toBlock": end_block,
                "topics": topics,
            }
        )
        for log in logs:
            if topics[0] == approval_for_all_topic:
                raw_data = log.get("data", b"")
                raw_hex = raw_data.hex() if hasattr(raw_data, "hex") else str(raw_data)
                if int(raw_hex or "0", 16) == 0:
                    continue
            tx_hash = log["transactionHash"]
            return tx_hash.hex() if hasattr(tx_hash, "hex") else str(tx_hash)
    return ""


def check_assignment1(
    student: Student,
    gh: GitHubHelper,
    w3: Web3,
    config: Assignment1Config,
) -> Assignment1Result:
    """Validate the current NFT Quest against protected instructor settings."""
    res = Assignment1Result(
        approval_required=config.require_approval,
        professor_nft_contract=config.professor_nft_contract,
    )
    wallets = [address.lower() for address in student.eth_addresses if address]
    if not wallets:
        res.status = "FAIL"
        res.note = "missing_eth_address"
        return res

    transfers = fetch_nft_transfers_for_wallets(
        wallets, config.start_block, config.end_block
    )
    evidence = evaluate_assignment1_transfers(transfers, wallets, config)
    professor_receive = evidence["professor_receive"]
    professor_return = evidence["professor_return"]
    personal_mint = evidence["personal_mint"]
    transfer_to_special = evidence["transfer_to_special"]

    res.professor_received_ok = professor_receive is not None
    res.professor_returned_ok = professor_return is not None
    res.personal_mint_ok = personal_mint is not None
    res.transfer_to_special_ok = transfer_to_special is not None

    if professor_receive:
        res.professor_token_id = str(professor_receive.get("tokenID", ""))
        res.professor_receive_tx_hash = str(professor_receive.get("hash", ""))
    if professor_return:
        res.professor_return_tx_hash = str(professor_return.get("hash", ""))
    if personal_mint:
        res.personal_nft_contract = str(personal_mint.get("contractAddress", ""))
        res.personal_token_id = str(personal_mint.get("tokenID", ""))
        res.personal_mint_tx_hash = str(personal_mint.get("hash", ""))
    if transfer_to_special:
        res.transfer_to_special_tx_hash = str(transfer_to_special.get("hash", ""))

    if not config.require_approval:
        res.approval_ok = True
    elif personal_mint:
        owner = str(personal_mint.get("to", ""))
        approval_end_block = (
            _int_field(transfer_to_special, "blockNumber")
            if transfer_to_special
            else min(config.end_block, w3.eth.block_number)
        )
        res.approval_tx_hash = find_erc721_approval(
            w3=w3,
            nft_contract=res.personal_nft_contract,
            owner=owner,
            approved_contract=config.special_contract,
            token_id=res.personal_token_id,
            start_block=max(config.start_block, _int_field(personal_mint, "blockNumber")),
            end_block=approval_end_block,
        )
        res.approval_ok = bool(res.approval_tx_hash)

    if student.github_raw:
        try:
            owner, repo, _ = resolve_repo(student.github_raw, gh)
            res.repo = f"{owner}/{repo}"
            repo_data = gh.get_repo(owner, repo)
            commits = gh.list_commits(owner, repo, per_page=5)
            res.github_ok = repo_data.get("archived") is False
            res.commits_ok = len(commits) > 0
        except Exception as exc:
            res.note = f"github_metadata_error={exc}"

    required_checks = [
        res.professor_received_ok,
        res.professor_returned_ok,
        res.personal_mint_ok,
        res.approval_ok,
        res.transfer_to_special_ok,
    ]
    if all(required_checks):
        res.status = "PASS"
    elif any(
        [
            res.professor_received_ok,
            res.professor_returned_ok,
            res.personal_mint_ok,
            bool(res.approval_tx_hash),
            res.transfer_to_special_ok,
        ]
    ):
        res.status = "PARTIAL"
    else:
        res.status = "FAIL"

    note_parts = [
        f"professor_receive={'PASS' if res.professor_received_ok else 'FAIL'}",
        f"professor_return={'PASS' if res.professor_returned_ok else 'FAIL'}",
        f"personal_mint={'PASS' if res.personal_mint_ok else 'FAIL'}",
        (
            "approval=NOT_REQUIRED"
            if not res.approval_required
            else f"approval={'PASS' if res.approval_ok else 'FAIL'}"
        ),
        f"special_transfer={'PASS' if res.transfer_to_special_ok else 'FAIL'}",
    ]
    if res.note:
        note_parts.append(res.note)
    res.note = "; ".join(note_parts)
    return res


def check_ethernaut(
    student: Student,
    completed_by_wallet: dict[str, dict[str, Any]],
    level_complexity: dict[str, int],
    level_addr_to_name: dict[str, str],
    repo_texts_cache: dict[str, dict[str, str]],
    gh: GitHubHelper,
    repo_hint: str = "",
    tx_fallback_by_wallet: dict[str, dict[str, Any]] | None = None,
) -> EthernautResult:
    res = EthernautResult()

    declared_levels: list[str] = []
    if repo_hint:
        try:
            owner, repo = repo_hint.split("/", 1)
            cache_key = f"{owner}/{repo}"
            texts = repo_texts_cache.get(cache_key)
            if texts is None:
                repo_data = gh.get_repo(owner, repo)
                texts = collect_repo_texts(gh, owner, repo, repo_data["default_branch"])
                repo_texts_cache[cache_key] = texts
            declared_levels = find_declared_levels_in_texts(
                texts, list(level_complexity.keys())
            )
        except Exception:
            pass
    res.declared_levels = declared_levels
    if declared_levels:
        res.declared_complexity = sum(
            level_complexity[level] for level in declared_levels
        )

    matched = None
    for wallet in student.eth_addresses:
        info = completed_by_wallet.get(wallet.lower())
        if info:
            if matched is None or len(info["level_addresses"]) > len(
                matched[1]["level_addresses"]
            ):
                matched = (wallet.lower(), info)

    if matched is None:
        # Safety net: Etherscan txlist can see Submit Level Instance transactions even
        # when RPC log parsing or current Ethernaut event mapping fails.
        if tx_fallback_by_wallet:
            best_wallet = ""
            best_info = None
            for wallet in student.eth_addresses:
                info = tx_fallback_by_wallet.get(wallet.lower())
                if info and (
                    best_info is None
                    or info.get("submit_count", 0) > best_info.get("submit_count", 0)
                ):
                    best_wallet = wallet.lower()
                    best_info = info
            if best_info:
                submit_count = int(best_info.get("submit_count", 0))
                level_names = list(best_info.get("level_names", []) or [])
                raw_level_addresses = list(
                    best_info.get("raw_level_addresses", []) or []
                )
                res.matched_wallet = best_wallet
                res.onchain_total_submits = submit_count
                res.submit_tx_hashes = list(best_info.get("submit_txs", []) or [])
                res.submit_blocks = list(best_info.get("submit_blocks", []) or [])
                res.methods = list(best_info.get("submit_methods", []) or [])
                res.submitted_instances = list(
                    best_info.get("submitted_instances", []) or []
                )
                res.raw_level_addresses = raw_level_addresses
                res.level_details = list(best_info.get("level_details", []) or [])

                if level_names:
                    res.onchain_levels = sorted(level_names)
                    res.onchain_unique_levels = len(set(level_names))
                    res.onchain_complexity = sum(
                        level_complexity.get(l, 0) for l in res.onchain_levels
                    )
                elif raw_level_addresses:
                    res.onchain_levels = [
                        f"Unknown level {i}"
                        for i in range(1, len(raw_level_addresses) + 1)
                    ]
                    res.onchain_unique_levels = len(raw_level_addresses)
                else:
                    # Last-resort evidence: real submitLevelInstance txs exist, but
                    # receipt did not expose parseable level names/addresses.
                    res.onchain_unique_levels = submit_count
                    res.onchain_levels = [
                        f"SubmitLevelInstance tx #{i}"
                        for i in range(1, submit_count + 1)
                    ]

                res.bonus_15_levels = res.onchain_unique_levels >= A2_BONUS_LEVELS
                if res.onchain_complexity is not None:
                    if res.onchain_complexity >= A2_PASS_COMPLEXITY:
                        res.status = "PASS"
                    elif res.onchain_unique_levels > 0:
                        res.status = "TRIED"
                    else:
                        res.status = "-"
                    res.note = "txlist+receipt fallback: submit txs found; complexity calculated from parsed LevelCompletedLog"
                else:
                    res.status = "TRIED" if submit_count > 0 else "-"
                    res.note = "txlist fallback: found real Submit Level Instance txs; level-name/complexity mapping unavailable"
                return res

        if declared_levels:
            res.status = "DECLARED ONLY"
            res.note = "repo has Ethernaut level names, but no completed logs matched student wallet"
        else:
            res.status = "-"
            res.note = "no matched Ethernaut activity"
        return res

    wallet, info = matched
    res.matched_wallet = wallet
    res.onchain_total_submits = int(info["count"])
    res.onchain_unique_levels = len(info["level_addresses"])
    res.onchain_levels = sorted(info["level_names"])
    if res.onchain_levels:
        res.onchain_complexity = sum(
            level_complexity[l] for l in res.onchain_levels if l in level_complexity
        )

    res.raw_level_addresses = (
        sorted(info.get("level_addresses", [])) if isinstance(info, dict) else []
    )
    res.bonus_15_levels = res.onchain_unique_levels >= A2_BONUS_LEVELS

    if res.onchain_complexity is not None:
        if res.onchain_complexity >= A2_PASS_COMPLEXITY:
            res.status = "PASS"
        elif res.onchain_unique_levels > 0:
            res.status = "TRIED"
        else:
            res.status = "-"
        if not level_addr_to_name:
            res.note = "on-chain levels mapped partially or not at all"
    else:
        if (
            res.declared_complexity is not None
            and res.declared_complexity >= A2_PASS_COMPLEXITY
            and res.onchain_unique_levels >= len(res.declared_levels)
        ):
            res.status = "PASS (declared+count)"
            res.note = "complexity from repo-declared levels; on-chain cross-check by unique completed level count"
        elif res.onchain_unique_levels > 0:
            res.status = "TRIED"
            res.note = (
                "on-chain completions found, but precise level-name mapping unavailable"
            )
        else:
            res.status = "-"
    return res


def result_cell(value: Any) -> Any:
    """Convert result values to cells accepted by the Google Sheets API."""
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def overall_status(
    student_id: str,
    scope: str,
    a1: Assignment1Result,
    a2: EthernautResult,
    errors: list[dict[str, str]],
) -> tuple[str, str]:
    student_errors = [item for item in errors if item.get("student_id") == student_id]
    if student_errors:
        stages = ", ".join(
            sorted({item.get("stage", "check") for item in student_errors})
        )
        return "ERROR", f"Technical error: {stages}"

    statuses: list[str] = []
    if scope in {"all", "assignment1"}:
        statuses.append(a1.status.upper())
    if scope in {"all", "ethernaut"}:
        statuses.append(a2.status.upper())

    if statuses and all(status == "PASS" for status in statuses):
        return "PASS", ""
    if any(
        status in {"PARTIAL", "TRIED", "DECLARED ONLY", "PASS (DECLARED+COUNT)"}
        for status in statuses
    ):
        return "REVIEW", "Evidence exists, but the result requires instructor review"
    return "FAIL", "Required evidence was not found"


def write_google_results(
    client: gspread.Client,
    results_folder_id: str,
    share_email: str,
    students: list[Student],
    a1_results: dict[str, Assignment1Result],
    a2_results: dict[str, EthernautResult],
    errors: list[dict[str, str]],
    run_mode: str,
    scope: str,
) -> tuple[str, str]:
    """Create a new result spreadsheet. The source spreadsheet is never edited."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    prefix = "FINAL_AUTOTEST" if run_mode == "final" else "PREVIEW_AUTOTEST"
    title = f"{prefix}_{timestamp}"
    spreadsheet = client.create(title, folder_id=results_folder_id or None)

    if share_email:
        try:
            spreadsheet.share(
                share_email, perm_type="user", role="writer", notify=False
            )
        except Exception as exc:
            errors.append(
                {
                    "student_id": "",
                    "name": "",
                    "stage": "share result spreadsheet",
                    "error": str(exc),
                }
            )

    summary_rows: list[list[Any]] = [
        [
            "Run mode",
            "Name",
            "ID",
            "Email",
            "GitHub",
            "Ethereum",
            "Polkadot",
            "TON",
            "Group",
            "Professor NFT received",
            "Professor NFT returned",
            "Personal NFT minted",
            "Approval",
            "Transferred to special contract",
            "Assignment 1",
            "Ethernaut",
            "A2 Complexity",
            "A2 Levels",
            "Autotest status",
            "Manual review",
        ]
    ]
    detail_rows: list[list[Any]] = [
        [
            "Name",
            "ID",
            "GitHub",
            "ETH addresses",
            "A1 repo",
            "GitHub reachable",
            "Commits found",
            "Professor NFT received",
            "Professor NFT returned",
            "Personal NFT minted",
            "Approval",
            "Transferred to special contract",
            "Assignment 1",
            "Professor NFT contract",
            "Professor token ID",
            "Personal NFT contract",
            "Personal token ID",
            "Professor receive tx",
            "Professor return tx",
            "Personal mint tx",
            "Approval tx",
            "Transfer to special tx",
            "A1 note",
            "Ethernaut",
            "Matched wallet",
            "Onchain unique levels",
            "Onchain total submits",
            "Onchain levels",
            "Onchain complexity",
            "A2 bonus",
            "A2 submit tx hashes",
            "A2 blocks",
            "A2 instances",
            "A2 level contracts",
            "A2 level details",
            "A2 methods",
            "Declared levels",
            "Declared complexity",
            "A2 note",
        ]
    ]
    review_rows: list[list[Any]] = [["Name", "ID", "Check", "Status", "Reason"]]

    for student in students:
        a1 = a1_results.get(student.student_id, Assignment1Result())
        a2 = a2_results.get(student.student_id, EthernautResult())
        final_status, review_reason = overall_status(
            student.student_id, scope, a1, a2, errors
        )
        a1_status = a1.status if scope in {"all", "assignment1"} else "NOT RUN"
        a2_status = a2.status if scope in {"all", "ethernaut"} else "NOT RUN"
        a1_selected = scope in {"all", "assignment1"}

        def a1_check_status(ok: bool) -> str:
            return "PASS" if ok else ("FAIL" if a1_selected else "NOT RUN")

        professor_receive_status = a1_check_status(a1.professor_received_ok)
        professor_return_status = a1_check_status(a1.professor_returned_ok)
        personal_mint_status = a1_check_status(a1.personal_mint_ok)
        if not a1_selected:
            approval_status = "NOT RUN"
        elif not a1.approval_required:
            approval_status = "NOT REQUIRED"
        else:
            approval_status = a1_check_status(a1.approval_ok)
        special_transfer_status = a1_check_status(a1.transfer_to_special_ok)

        summary_rows.append(
            [
                run_mode.upper(),
                student.name,
                student.student_id,
                student.email,
                student.github_raw,
                ", ".join(student.eth_addresses),
                student.polkadot_address,
                student.ton_address,
                student.group,
                professor_receive_status,
                professor_return_status,
                personal_mint_status,
                approval_status,
                special_transfer_status,
                a1_status,
                a2_status,
                a2.onchain_complexity,
                a2.onchain_unique_levels,
                final_status,
                review_reason,
            ]
        )
        detail_rows.append(
            [
                student.name,
                student.student_id,
                student.github_raw,
                ", ".join(student.eth_addresses),
                a1.repo,
                a1.github_ok,
                a1.commits_ok,
                professor_receive_status,
                professor_return_status,
                personal_mint_status,
                approval_status,
                special_transfer_status,
                a1_status,
                a1.professor_nft_contract,
                a1.professor_token_id,
                a1.personal_nft_contract,
                a1.personal_token_id,
                a1.professor_receive_tx_hash,
                a1.professor_return_tx_hash,
                a1.personal_mint_tx_hash,
                a1.approval_tx_hash,
                a1.transfer_to_special_tx_hash,
                a1.note,
                a2_status,
                a2.matched_wallet,
                a2.onchain_unique_levels,
                a2.onchain_total_submits,
                ", ".join(a2.onchain_levels),
                a2.onchain_complexity,
                "YES" if a2.bonus_15_levels else "NO",
                ", ".join(a2.submit_tx_hashes),
                ", ".join(map(str, a2.submit_blocks)),
                ", ".join(a2.submitted_instances),
                ", ".join(a2.raw_level_addresses),
                " || ".join(a2.level_details),
                ", ".join(a2.methods),
                ", ".join(a2.declared_levels),
                a2.declared_complexity,
                a2.note,
            ]
        )
        if final_status != "PASS":
            review_rows.append(
                [student.name, student.student_id, scope, final_status, review_reason]
            )

    error_rows: list[list[Any]] = [["Name", "ID", "Stage", "Error"]]
    for item in errors:
        error_rows.append(
            [
                item.get("name", ""),
                item.get("student_id", ""),
                item.get("stage", ""),
                item.get("error", ""),
            ]
        )

    worksheets = [
        (spreadsheet.sheet1, "Closed list", summary_rows),
        (None, "Autotest details", detail_rows),
        (None, "Manual review", review_rows),
        (None, "Errors", error_rows),
    ]
    for existing, sheet_name, rows in worksheets:
        column_count = max(len(rows[0]), 1)
        row_count = max(len(rows), 2)
        worksheet = existing or spreadsheet.add_worksheet(
            title=sheet_name,
            rows=row_count,
            cols=column_count,
        )
        if existing:
            worksheet.update_title(sheet_name)
            worksheet.resize(rows=row_count, cols=column_count)
        worksheet.update(
            values=[[result_cell(value) for value in row] for row in rows],
            range_name="A1",
            value_input_option="RAW",
        )
        spreadsheet.batch_update(
            {
                "requests": [
                    {
                        "updateSheetProperties": {
                            "properties": {
                                "sheetId": worksheet.id,
                                "gridProperties": {"frozenRowCount": 1},
                            },
                            "fields": "gridProperties.frozenRowCount",
                        }
                    },
                    {
                        "repeatCell": {
                            "range": {
                                "sheetId": worksheet.id,
                                "startRowIndex": 0,
                                "endRowIndex": 1,
                            },
                            "cell": {
                                "userEnteredFormat": {
                                    "backgroundColor": {
                                        "red": 0.15,
                                        "green": 0.45,
                                        "blue": 0.30,
                                    },
                                    "textFormat": {
                                        "foregroundColor": {
                                            "red": 1,
                                            "green": 1,
                                            "blue": 1,
                                        },
                                        "bold": True,
                                    },
                                }
                            },
                            "fields": "userEnteredFormat(backgroundColor,textFormat)",
                        }
                    },
                    {
                        "autoResizeDimensions": {
                            "dimensions": {
                                "sheetId": worksheet.id,
                                "dimension": "COLUMNS",
                                "startIndex": 0,
                                "endIndex": column_count,
                            }
                        }
                    },
                ]
            }
        )

    return title, f"https://docs.google.com/spreadsheets/d/{spreadsheet.id}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Read the protected course roster and create a new Google Sheet with autotest results"
    )
    parser.add_argument(
        "--spreadsheet-id", default=os.getenv("COURSE_STUDENTS_SPREADSHEET_ID", "")
    )
    parser.add_argument(
        "--students-sheet",
        default=os.getenv("COURSE_STUDENTS_WORKSHEET", "COURSE_STUDENTS"),
    )
    parser.add_argument(
        "--ethernaut-sheet",
        default=os.getenv("ETHERNAUT_LEVELS_WORKSHEET", "ETHERNAUT_LEVELS"),
    )
    parser.add_argument(
        "--assignment1-sheet",
        default=os.getenv("ASSIGNMENT1_CONFIG_WORKSHEET", "ASSIGNMENT1_CONFIG"),
    )
    parser.add_argument(
        "--results-folder-id", default=os.getenv("GOOGLE_RESULTS_FOLDER_ID", "")
    )
    parser.add_argument(
        "--share-email", default=os.getenv("GOOGLE_RESULTS_SHARE_EMAIL", "")
    )
    parser.add_argument("--mode", choices=["preview", "final"], default="preview")
    parser.add_argument(
        "--scope", choices=["all", "assignment1", "ethernaut"], default="all"
    )
    parser.add_argument(
        "--rpc",
        default=os.getenv("SEPOLIA_RPC_URL", "").strip()
        or "https://ethereum-sepolia-rpc.publicnode.com",
    )
    parser.add_argument(
        "--ethernaut-address", default="0xa3e7317e591d5a0f1c605be1b3ac4d2ae56104d6"
    )
    parser.add_argument(
        "--start-block", type=int, default=env_int("ETHERNAUT_START_BLOCK", 0)
    )
    args = parser.parse_args()

    service_account_json = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    if not service_account_json:
        raise ValueError("GOOGLE_SERVICE_ACCOUNT_JSON is required")
    if not args.spreadsheet_id:
        raise ValueError("COURSE_STUDENTS_SPREADSHEET_ID is required")
    if not args.results_folder_id:
        raise ValueError("GOOGLE_RESULTS_FOLDER_ID is required")

    client = google_client(service_account_json)
    print("[INFO] Loading active students from the protected Google Sheet...")
    students = read_students_from_google_sheet(
        client, args.spreadsheet_id, args.students_sheet
    )
    level_complexity, level_addr_to_name = read_ethernaut_config_from_google_sheet(
        client, args.spreadsheet_id, args.ethernaut_sheet
    )
    assignment1_config: Assignment1Config | None = None
    assignment1_config_error = ""
    if args.scope in {"all", "assignment1"}:
        try:
            assignment1_config = read_assignment1_config_from_google_sheet(
                client, args.spreadsheet_id, args.assignment1_sheet
            )
        except Exception as exc:
            assignment1_config_error = str(exc)
    print(f"[INFO] Students loaded: {len(students)}")
    print(f"[INFO] Ethernaut level rules loaded: {len(level_complexity)}")
    if assignment1_config:
        print("[INFO] Assignment 1 NFT Quest settings loaded")
    elif assignment1_config_error:
        print(f"[WARN] Assignment 1 config is invalid: {assignment1_config_error}")

    gh = GitHubHelper(os.getenv("GITHUB_TOKEN"))
    errors: list[dict[str, str]] = []
    w3: Web3 | None = None
    try:
        print("[INFO] Connecting to Sepolia RPC...")
        w3 = build_web3(args.rpc)
    except Exception as exc:
        errors.append(
            {"student_id": "", "name": "", "stage": "Sepolia RPC", "error": str(exc)}
        )
        print(f"[WARN] Sepolia RPC is unavailable: {exc}")

    completed_by_wallet: dict[str, dict[str, Any]] = {}
    tx_fallback_by_wallet: dict[str, dict[str, Any]] = {}
    ethernaut_logs_available = False
    ethernaut_fallback_available = False
    if args.scope in {"all", "ethernaut"}:
        if w3 is not None:
            try:
                print("[INFO] Downloading Ethernaut completed logs...")
                logs = get_ethernaut_logs(
                    w3, args.ethernaut_address, start_block=args.start_block
                )
                completed_by_wallet = parse_completed_logs(logs, level_addr_to_name)
                ethernaut_logs_available = True
                print(f"[INFO] Wallets with Ethernaut logs: {len(completed_by_wallet)}")
            except Exception as exc:
                errors.append(
                    {
                        "student_id": "",
                        "name": "",
                        "stage": "Ethernaut logs",
                        "error": str(exc),
                    }
                )
                print(f"[WARN] Ethernaut log scan failed: {exc}")

        if os.getenv("ETHERSCAN_API_KEY", "").strip():
            try:
                print(
                    "[INFO] Downloading Ethernaut transaction fallback from Etherscan..."
                )
                all_wallets = [
                    address for student in students for address in student.eth_addresses
                ]
                tx_fallback_by_wallet = fetch_ethernaut_tx_fallback(
                    wallets=all_wallets,
                    ethernaut_address=args.ethernaut_address,
                    start_block=args.start_block,
                )
                ethernaut_fallback_available = True
                if w3 is not None and tx_fallback_by_wallet:
                    enrich_ethernaut_tx_fallback_with_receipts(
                        w3,
                        tx_fallback_by_wallet,
                        args.ethernaut_address,
                        level_addr_to_name,
                    )
            except Exception as exc:
                errors.append(
                    {
                        "student_id": "",
                        "name": "",
                        "stage": "Ethernaut Etherscan",
                        "error": str(exc),
                    }
                )
                print(f"[WARN] Ethernaut Etherscan fallback failed: {exc}")
        else:
            print("[WARN] ETHERSCAN_API_KEY is not set; Ethernaut fallback is disabled")

    repo_texts_cache: dict[str, dict[str, str]] = {}
    a1_results: dict[str, Assignment1Result] = {}
    a2_results: dict[str, EthernautResult] = {}

    for idx, student in enumerate(students, start=1):
        print(
            f"[INFO] [{idx}/{len(students)}] Checking {student.student_id} | {student.name}"
        )
        a1 = Assignment1Result(status="NOT RUN")
        if args.scope in {"all", "assignment1"}:
            if assignment1_config is None:
                a1 = Assignment1Result(
                    status="ERROR", note=assignment1_config_error or "missing config"
                )
                errors.append(
                    {
                        "student_id": student.student_id,
                        "name": student.name,
                        "stage": "Assignment 1 config",
                        "error": assignment1_config_error or "missing config",
                    }
                )
            elif w3 is None:
                a1 = Assignment1Result(status="ERROR", note="Sepolia RPC unavailable")
                errors.append(
                    {
                        "student_id": student.student_id,
                        "name": student.name,
                        "stage": "Assignment 1",
                        "error": "Sepolia RPC unavailable",
                    }
                )
            else:
                try:
                    a1 = check_assignment1(student, gh, w3, assignment1_config)
                except Exception as exc:
                    a1 = Assignment1Result(status="ERROR", note=str(exc))
                    errors.append(
                        {
                            "student_id": student.student_id,
                            "name": student.name,
                            "stage": "Assignment 1",
                            "error": str(exc),
                        }
                    )
        a1_results[student.student_id] = a1

        a2 = EthernautResult(status="NOT RUN")
        if args.scope in {"all", "ethernaut"}:
            if not ethernaut_logs_available and not ethernaut_fallback_available:
                message = "Both Ethernaut evidence sources are unavailable"
                a2 = EthernautResult(status="ERROR", note=message)
                errors.append(
                    {
                        "student_id": student.student_id,
                        "name": student.name,
                        "stage": "Ethernaut",
                        "error": message,
                    }
                )
            else:
                try:
                    a2 = check_ethernaut(
                        student=student,
                        completed_by_wallet=completed_by_wallet,
                        level_complexity=level_complexity,
                        level_addr_to_name=level_addr_to_name,
                        repo_texts_cache=repo_texts_cache,
                        gh=gh,
                        repo_hint=a1.repo,
                        tx_fallback_by_wallet=tx_fallback_by_wallet,
                    )
                except Exception as exc:
                    a2 = EthernautResult(status="ERROR", note=str(exc))
                    errors.append(
                        {
                            "student_id": student.student_id,
                            "name": student.name,
                            "stage": "Ethernaut",
                            "error": str(exc),
                        }
                    )
        a2_results[student.student_id] = a2

    print("[INFO] Creating a new Google Sheet with results...")
    output_title, output_url = write_google_results(
        client=client,
        results_folder_id=args.results_folder_id,
        share_email=args.share_email,
        students=students,
        a1_results=a1_results,
        a2_results=a2_results,
        errors=errors,
        run_mode=args.mode,
        scope=args.scope,
    )

    passed_a1 = sum(1 for x in a1_results.values() if x.status == "PASS")
    passed_a2 = sum(1 for x in a2_results.values() if x.status == "PASS")
    print(f"[OK] Assignment 1 PASS count: {passed_a1}")
    print(f"[OK] Ethernaut PASS count: {passed_a2}")
    print(f"[OK] Result spreadsheet: {output_title}")
    print(f"[OK] Result URL: {output_url}")
    github_output = os.getenv("GITHUB_OUTPUT", "").strip()
    if github_output:
        with Path(github_output).open("a", encoding="utf-8") as output_file:
            output_file.write(f"result_title={output_title}\n")
            output_file.write(f"result_url={output_url}\n")
    if not level_addr_to_name:
        print(
            "[WARN] ETHERNAUT_LEVELS has no address mapping; Ethernaut results may require manual review."
        )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Interrupted by user")
        sys.exit(1)
    except Exception as exc:
        print(f"\n[ERROR] {exc}")
        sys.exit(1)
