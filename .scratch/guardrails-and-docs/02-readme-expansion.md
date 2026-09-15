# 02: Expand README.md with setup and usage documentation

**What to build:** Extend README.md from its current 2-line state into a proper project guide. Add sections for Python setup (virtual environment, installation via requirements.txt), how to run tests, and how to run the scraper. Include a note about the `src/` directory being the Python package root.

**Blocked by:** 01: Create requirements.txt with all dependencies

**Status:** ready-for-agent

- [ ] Add "Setup" section to README with Python version requirement, virtual environment instructions, and `pip install -r requirements.txt` command
- [ ] Add "Running Tests" section explaining that tests must be run from `src/` directory and showing the command: `cd src && pytest tests/ -v`
- [ ] Add "Running the Scraper" section showing how to execute the workflow with environment variables (NEO4J_*, DWZ_*)
- [ ] Add "Project Structure" section briefly explaining the src/ layout and what each module does
- [ ] Verify README is readable and contains no outdated information
