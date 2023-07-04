.PHONY: mypyinstall
mypyinstall:
	pip install --upgrade pip
	pip install --upgrade --upgrade-strategy eager -r requirements-mypy.txt

.PHONY: ruffinstall
ruffinstall:
	pip install --upgrade pip
	pip install --upgrade --upgrade-strategy eager -r requirements-ruff.txt

.PHONY: install
install:
	pip install --upgrade pip
	pip install --upgrade --upgrade-strategy eager -r requirements.txt

.PHONY: test
test: rufftest typingtest

.PHONY: rufftest
rufftest:
	ruff .

.PHONY: typingtest
typingtest:
	mypy .
