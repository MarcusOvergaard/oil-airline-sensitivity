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

## Phase 3 - Cleaning, Returns, and Tableau Dataset

- Implemented and ran `notebooks/02_data_cleaning_and_returns.ipynb`.
- Loaded `data/raw/raw_prices.csv`, parsed `Date`, set it as the index, sorted by date, and validated all expected assets.
- Missing values were reported but not blindly forward-filled before return calculation.
- Weekly and monthly prices were built using the last available price in each period; returns were calculated from those resampled price series.
- Created airline excess returns as airline return minus S&P 500 return.
- Created `data/processed/weekly_returns.csv`, `data/processed/monthly_returns.csv`, `data/processed/weekly_excess_returns.csv`, and `data/processed/monthly_excess_returns.csv`.
- Created `data/tableau/airline_oil_tableau_dataset.csv` with airline rows only, including matching Brent return and S&P 500 return for each date and frequency.
- Issue noted: raw daily data contains missing values from different trading calendars and market holidays; after period-end resampling and first-return removal, the return and Tableau outputs contain no missing values.

## Phase 4 - Analysis, Oil Sensitivity, and Oil Shocks

- Implemented and ran `notebooks/03_analysis.ipynb`.
- Created visuals for normalized monthly performance, weekly correlations, monthly correlations, and oil sensitivity rankings.
- Estimated simple Brent-return sensitivity regressions for weekly returns, monthly returns, weekly excess returns, and monthly excess returns.
- Created `data/processed/oil_sensitivity_summary.csv` with alpha, beta, r-squared, p-value, significance flag, beta rank, beta confidence score, and plain-English interpretation.
- Created `data/processed/oil_shock_summary.csv` using top-20% positive Brent-return periods as oil shocks.
- Issue noted: explanatory power is generally weak; the strongest relationship is still low-r-squared, so oil sensitivity should be interpreted cautiously.

## Phase 4.5 - Market-Controlled Oil Sensitivity

- Added market-controlled regressions to `notebooks/03_analysis.ipynb` because Phase 4 showed weak explanatory power and some positive oil betas.
- Estimated `Airline Return = alpha + oil_beta × Brent Return + market_beta × S&P 500 Return` for weekly and monthly returns.
- Created `data/processed/oil_market_sensitivity_summary.csv` and `images/market_controlled_oil_beta_ranking.png`.
- After controlling for the S&P 500, monthly oil betas were not statistically significant for any airline.
- Weekly oil beta remained significant for Ryanair and American Airlines only; both were negative.
- Market beta was statistically significant for all airlines and both frequencies, and it was larger than oil beta in absolute terms in every row.
- Surprising result: Ryanair's positive monthly oil beta from the simple regression disappeared after market control, suggesting the earlier positive oil relationship was likely market-driven rather than oil-specific.

## Phase 5 - Tableau Export Validation

- Implemented and ran `notebooks/04_tableau_export_validation.ipynb`.
- Validated `data/tableau/airline_oil_tableau_dataset.csv`, `data/processed/oil_sensitivity_summary.csv`, `data/processed/oil_shock_summary.csv`, and `data/processed/oil_market_sensitivity_summary.csv`.
- Created `data/processed/tableau_validation_report.md`.
- Validation passed for file existence, required columns, row counts, missing values, frequency coverage, airline coverage, numeric fields, date parsing, and populated classification fields.
- Final readiness status: ready for Tableau dashboard building.
- Limitation noted: validation confirms schema, completeness, coverage, and basic type integrity; it does not re-run the underlying analytical regressions.

## Open Notes

- Hedging classifications are simplified and should be treated as exploratory labels, not definitive current operating facts.
- Monthly results should be treated as the primary interpretation layer; weekly results are a robustness check.
