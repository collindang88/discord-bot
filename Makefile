py-fmt:
	autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src/
	isort src/
	black src/
	@tput setaf 2; echo "Formatting done!"; tput sgr0

py-lint:
	flake8 src/
	@tput setaf 2; echo "Linting done!"; tput sgr0