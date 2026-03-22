#!/usr/bin/env bash
set -euo pipefail

rm -f artifacts/agent_output.log artifacts/score.json debug.txt || true
mkdir -p artifacts
: > artifacts/agent_output.log
