py-fmt:
	autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src/
	isort src/
	black src/
