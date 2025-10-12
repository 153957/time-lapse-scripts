.PHONY: tyinstall
tyinstall:
	uv pip install --upgrade -r requirements-ty.txt

.PHONY: ruffinstall
ruffinstall:
	uv pip install --upgrade -r requirements-ruff.txt

.PHONY: install
install:
	uv pip install --upgrade -r requirements.txt

.PHONY: test
test: rufftest typingtest

.PHONY: rufftest
rufftest:
	ruff check .
	ruff format --check .

.PHONY: typingtest
typingtest:
	ty check
