SRC_DIR = src/

.PHONY: ls py-fmt py-lint all

ls:
	@echo "Available targets:"
	@echo "  make install-deps    Install package depedencies"
	@echo "  make py-fmt          Format the code"
	@echo "  make py-lint         Lint the code"
	@echo "  make check           Format and lint the code"

install-deps:
	@pip install -r requirements.txt

py-fmt:
	@autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place $(SRC_DIR)
	@isort $(SRC_DIR)
	@black $(SRC_DIR)
	@tput setaf 2; echo "Formatting done!"; tput sgr0

py-lint:
	@flake8 $(SRC_DIR)
	@tput setaf 2; echo "Linting done!"; tput sgr0

check: py-fmt py-lint
