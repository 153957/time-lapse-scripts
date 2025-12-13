.PHONY: test
test: rufftest typingtest

.PHONY: rufftest
rufftest:
	uv run ruff check .
	uv run ruff format --check .

.PHONY: typingtest
typingtest:
	uv run ty check
