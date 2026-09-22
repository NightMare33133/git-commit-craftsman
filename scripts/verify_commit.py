#!/usr/bin/env python3
"""
git-commit-craftsman deterministic verification gate.
Exits 0 on success, exits 1 on rule violation with actionable failure diagnostic.
"""

import sys
import re

ALLOWED_TYPES = {"feat", "fix", "refactor", "perf", "docs", "style", "test", "chore"}
BANNED_SCOPES = {"misc", "all", "code", "patch", "fix"}
PAST_TENSE_VERBS = {
    "added", "adds", "adding",
    "fixed", "fixes", "fixing",
    "updated", "updates", "updating",
    "removed", "removes", "removing",
    "refactored", "refactors", "refactoring",
    "resolved", "resolves", "resolving",
    "prevented", "prevents", "preventing",
    "implemented", "implements", "implementing",
    "changed", "changes", "changing",
    "optimized", "optimizes", "optimizing",
}

HEADER_REGEX = re.compile(r"^([a-z]+)\(([a-z0-9_.\-]+)\)(!?):\s*(.+)$")

def verify_commit(msg: str) -> tuple[bool, list[str]]:
    errors = []
    lines = msg.strip().splitlines()
    if not lines:
        return False, ["Commit message cannot be empty."]

    header = lines[0].strip()

    # 1. 50-character ceiling rule
    header_len = len(header)
    if header_len > 50:
        errors.append(f"Header exceeds 50-character ceiling: detected {header_len} characters ({header_len - 50} chars over limit). Header was: '{header}'.")

    # 2. Match Conventional Commit structure
    m = HEADER_REGEX.match(header)
    if not m:
        errors.append(f"Header does not match '<type>(<scope>): <subject>' format. Received: '{header}'.")
        return False, errors

    c_type, c_scope, c_breaking, c_subject = m.groups()

    # 3. Type check
    if c_type not in ALLOWED_TYPES:
        errors.append(f"Invalid type '{c_type}'. Must be one of: {sorted(ALLOWED_TYPES)}.")

    # 4. Scope check
    if c_scope in BANNED_SCOPES:
        errors.append(f"Prohibited lazy scope '{c_scope}'. Scope must reflect concrete module or directory.")

    # 5. Subject casing & punctuation
    if not c_subject:
        errors.append("Subject line cannot be empty.")
    else:
        if c_subject[0].isupper():
            errors.append(f"Subject must start with a lowercase letter, found uppercase: '{c_subject[0]}' in '{c_subject}'.")
        if c_subject.endswith(".") or c_subject.endswith("!"):
            errors.append(f"Subject must NOT end with punctuation (., !). Found: '{c_subject[-1]}'.")

        # 6. Imperative mood check
        first_word = re.split(r"[^a-zA-Z]", c_subject)[0].lower()
        if first_word in PAST_TENSE_VERBS:
            errors.append(f"Subject verb must be bare imperative (e.g. 'add', 'fix'), not past/third-person. Found: '{first_word}'.")

    # 7. Breaking change footer validation if ! present
    if c_breaking == "!" and len(lines) > 1:
        has_breaking_footer = any(line.startswith("BREAKING CHANGE:") for line in lines[1:])
        if not has_breaking_footer:
            errors.append("Breaking change indicated with '!', but missing mandatory 'BREAKING CHANGE: <explanation>' in footer.")

    return len(errors) == 0, errors

def run_self_test():
    print("=== Running git-commit-craftsman Verification Gate Self-Test ===")
    test_cases = [
        # (msg, expected_pass, description)
        ("fix(auth): refresh token 60s before expiration", True, "Valid atomic fix"),
        ("feat(ui): add dark mode toggle switch", True, "Valid atomic feat"),
        ("feat(api)!: remove v1 endpoints", True, "Valid single-line breaking change"),
        ("fix(auth): ensure that all user session authentication tokens refresh properly", False, "Exceeds 50 chars"),
        ("fix(auth): fixed the token expiration bug", False, "Past tense verb 'fixed'"),
        ("feat(misc): add some utilities", False, "Banned lazy scope 'misc'"),
        ("style(home): update button label.", False, "Ends with period"),
        ("feat(auth): Add google login", False, "Uppercase start letter"),
    ]

    all_passed = True
    for msg, expected_pass, desc in test_cases:
        passed, errors = verify_commit(msg)
        if passed == expected_pass:
            status = "✅ PASS"
        else:
            status = "❌ FAIL"
            all_passed = False
        print(f"[{status}] {desc} -> len: {len(msg.splitlines()[0])} | errors: {errors}")

    if all_passed:
        print("\n🎉 ALL SELF-TEST SUITES PASSED DETERMINISTICALLY!")
        return 0
    else:
        print("\n⚠️ SELF-TEST SUITE FAILED!")
        return 1

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        sys.exit(run_self_test())

    if len(sys.argv) < 2:
        # Read from stdin
        raw_msg = sys.stdin.read()
    else:
        raw_msg = sys.argv[1]

    passed, errors = verify_commit(raw_msg)
    if passed:
        print("✅ [GATE APPROVED] Commit message strictly satisfies all craftsman rules.")
        sys.exit(0)
    else:
        print("❌ [GATE REJECTED] Commit message violated craftsman rules:")
        for err in errors:
            print(f"   • {err}")
        print("\nAction Required: Fix the violations above before emitting the final commit command.")
        sys.exit(1)
