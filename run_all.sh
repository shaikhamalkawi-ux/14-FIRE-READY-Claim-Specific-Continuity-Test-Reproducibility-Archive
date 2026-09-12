#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 test_socr_adapter.py
python3 validate_socr_against_rules.py
echo "ALL REPRODUCIBILITY CHECKS PASS"
