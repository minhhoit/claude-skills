#!/usr/bin/env python3
"""Heuristic linter for YouTube scripts: flags phrasing that tends to trip
AI-content / misinformation policy. Stdlib only. Heuristic aid, not a judge.

Usage:
    python policy_lint.py path/to/script.txt
    cat script.txt | python policy_lint.py -
"""
import re
import sys

# (pattern, risk label, why it matters)
RULES = [
    (r"\b(they don'?t want you to know|hidden truth|suppressed|forbidden history|cover[- ]?up|the truth about)\b",
     "conspiracy-framing", "Sounds like 'suppressed truth' framing -> misinformation risk. Reframe as 'lesser-known'."),
    (r"\b(scientists? proved|100%|guaranteed|always|never|everyone knows|it'?s a fact that)\b",
     "absolute-claim", "Absolute/unsourced claim. Soften or cite a real basis."),
    (r"\b(secret|shocking truth|they lied|real reason)\b",
     "sensational", "Sensational hook can clash with the actual payoff -> misleading-metadata risk."),
    (r"\b(cure|miracle|kills? the virus|doctors hate)\b",
     "medical/dangerous", "Medical or dangerous-claim territory. Remove or heavily qualify."),
]


def lint(text):
    findings = []
    for i, line in enumerate(text.splitlines(), 1):
        for pattern, label, why in RULES:
            for m in re.finditer(pattern, line, flags=re.IGNORECASE):
                findings.append((i, label, m.group(0), why))
    return findings


def main():
    if len(sys.argv) != 2:
        print("usage: python policy_lint.py <file|->", file=sys.stderr)
        return 2
    src = sys.argv[1]
    text = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    findings = lint(text)
    if not findings:
        print("Policy lint: no risky phrasing detected (heuristic only — still do the manual Step 1 review).")
        return 0
    print(f"Policy lint: {len(findings)} flag(s) — review before upload:\n")
    for line_no, label, hit, why in findings:
        print(f"  line {line_no} [{label}] \"{hit}\"")
        print(f"      -> {why}\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
