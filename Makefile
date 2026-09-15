.PHONY: help install test verify run

help:
	@echo "Available commands:"
	@echo "  make install      - Install dependencies from requirements.txt"
	@echo "  make test         - Run test suite"
	@echo "  make verify       - Verify all modules load correctly"
	@echo "  make run          - Run the scraper workflow"
	@echo ""
	@echo "Note: On Windows without GNU make, run commands directly:"
	@echo "  cd src ^&^& pytest tests/ -v"
	@echo "  cd src ^&^& python -m black --check ."
	@echo "  cd src ^&^& python -m ruff check ."

install:
	pip install -r requirements.txt

test:
	cd src && pytest tests/ -v

verify:
	cd src && python -c "from scraping.extractors import ClubRosterScraper, PlayerHistoryScraper, TournamentDetailScraper; from normalize.normalizer import Normalizer; from storage.neo4j_client import Neo4jClient; print('✓ All core modules verified successfully')"

run:
	cd src && python main.py
