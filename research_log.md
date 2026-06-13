# Research Log

This log records research decisions, data-source notes, assumptions, and validation findings for the project.

## Phase 1 - Repository Setup

- Created the project folder structure required by `project_plan.md`.
- Added placeholder notebooks only; no data was downloaded and no analysis code was implemented.
- Data source planned: Yahoo Finance via `yfinance`.

## Phase 2 - Raw Data Collection

- Implemented and ran `notebooks/01_data_collection.ipynb`.
- Downloaded adjusted close price data from Yahoo Finance using `yfinance` for Brent Oil, Ryanair, Lufthansa, Southwest, American Airlines, and the S&P 500.
- Saved raw adjusted price data to `data/raw/raw_prices.csv`.
- Validation passed: the CSV exists, includes all expected assets, has a `Date` index, and is not empty.
- Data issue noticed: missing values are present across all assets, likely because of different trading calendars, market holidays, and ticker-specific availability. Missing values were reported but not cleaned in Phase 2.

## Open Notes

- Hedging classifications are simplified and should be treated as exploratory labels, not definitive current operating facts.
- Monthly results should be treated as the primary interpretation layer; weekly results are a robustness check.
