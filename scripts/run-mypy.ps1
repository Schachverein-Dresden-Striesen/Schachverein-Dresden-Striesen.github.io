# Wrapper script for mypy to handle lint-staged file argument passing
# Usage: Called by lint-staged, ignores file arguments and checks entire src/

param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Files
)

# Run mypy on the entire src/ directory, ignoring any files passed by lint-staged
python -m mypy src/ --ignore-missing-imports

exit $LASTEXITCODE
