# Notes

- Club: Schachverein Dresden-Striesen
- Source website: https://www.schachbund.de/dwz-vereine/F2810.html
- Goal: preserve the tournament history of club players over time.
- Data model terms in use:
  - player
  - tournament
  - season
  - result
  - source page / raw snapshot
- Current collection pattern: fetch club roster pages, follow each player, harvest tournament history, and store normalized records plus raw HTML snapshots.
- Human review is reserved for changed or ambiguous records, not for every page fetch.
