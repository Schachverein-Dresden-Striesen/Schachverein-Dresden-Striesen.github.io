# 06: Add Husky pre-commit hooks with lint-staged and formatting

**What to build:** Set up Husky pre-commit hooks that run linting and formatting checks before code is committed. This catches style violations and obvious issues at commit time rather than later in CI, giving immediate feedback and keeping the codebase consistent.

**Blocked by:** 05: Add pyproject.toml with pytest configuration and metadata

**Status:** ready-for-agent

- [ ] Install Husky and initialize `.husky/` directory structure
- [ ] Create `.husky/pre-commit` hook that runs `lint-staged`
- [ ] Configure `.lintstagedrc.json` to:
  - Run `black` on `*.py` files (format only, no write)
  - Run `ruff check --fix` on `*.py` files for fixable violations
  - Run `ruff check` on `*.py` files for reporting unfixable violations
- [ ] Add Husky dev dependency to `pyproject.toml` if using it as lock file
- [ ] Document in README that developers should run `make install` or manual setup to enable hooks
- [ ] Verify pre-commit hook runs on a test commit and blocks commits with formatting violations
- [ ] Ensure hook can be skipped with `git commit --no-verify` if needed (for WIP commits, etc.)
