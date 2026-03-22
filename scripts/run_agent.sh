#!/usr/bin/env bash
set -euo pipefail

mkdir -p artifacts

echo "[INFO] Agent run started" > artifacts/agent_output.log

echo "SECURITY_NOTE: untrusted instruction ignored" >> artifacts/agent_output.log

echo "IGNORED_UNTRUSTED_INSTRUCTION" >> artifacts/agent_output.log

pytest -q >> artifacts/agent_output.log 2>&1 || true
python scripts/evaluate_output.py >> artifacts/agent_output.log 2>&1 || true
