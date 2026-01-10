.PHONY: test
test: rufftest typingtest

.PHONY: rufftest
rufftest:
	uv run ruff check .
	uv run ruff format --check .

.PHONY: rufffix
rufftest:
	uv run ruff check --fix-only .
	uv run ruff format .

.PHONY: typingtest
typingtest:
	uv run ty check
