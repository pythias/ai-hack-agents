reset:
	bash scripts/reset_sandbox.sh

check:
	pytest -q && python scripts/evaluate_output.py

run-agent:
	bash scripts/run_agent.sh
