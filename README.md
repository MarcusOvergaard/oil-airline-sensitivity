# Fuel, Hedging, and Business Models

## Overview

This project analyzes whether different airline business models show different sensitivities to oil price changes. It compares selected airline stocks against Brent crude oil futures and the S&P 500 using Python-based analysis and a planned Tableau dashboard.

The project is exploratory. It is designed to demonstrate data analysis skills and generate useful investing questions, not to prove a predetermined thesis or provide investment advice.

## Research Question

How sensitive are different airline business models to changes in oil prices?

## Assets

Oil benchmark:

- Brent Crude Oil Futures: `BZ=F`

Airlines:

- Ryanair: `RYAAY` — Europe, low-cost, historically higher hedging
- Lufthansa: `LHA.DE` — Europe, legacy, mixed/moderate hedging
- Southwest Airlines: `LUV` — United States, low-cost, historically strong hedging
- American Airlines: `AAL` — United States, legacy, historically lower hedging

Market benchmark:

- S&P 500: `^GSPC`

## Time Period

The analysis starts on `2018-01-01` and uses the latest available data at the time of collection.

## Methodology

The project will:

1. Download price data from Yahoo Finance using `yfinance`.
2. Calculate weekly and monthly returns.
3. Calculate airline excess returns relative to the S&P 500.
4. Compare normalized performance starting at 100.
5. Analyze weekly and monthly correlations.
6. Estimate oil sensitivity using simple linear regression:

   `airline_return = alpha + beta * brent_return`

7. Compare airline behavior during oil shock periods, defined as the top 20% of positive Brent returns.
8. Export a Tableau-ready dataset for dashboard development.

## Planned Outputs

Raw data:

- `data/raw/raw_prices.csv`

Processed data:

- `data/processed/weekly_returns.csv`
- `data/processed/monthly_returns.csv`
- `data/processed/weekly_excess_returns.csv`
- `data/processed/monthly_excess_returns.csv`
- `data/processed/oil_sensitivity_summary.csv`
- `data/processed/oil_shock_summary.csv`

Tableau data:

- `data/tableau/airline_oil_tableau_dataset.csv`

## Repository Structure

```text
data/
  raw/
  processed/
  tableau/
notebooks/
  01_data_collection.ipynb
  02_data_cleaning_and_returns.ipynb
  03_analysis.ipynb
  04_tableau_export_validation.ipynb
src/
  config.py
images/
tableau/
  dashboard_plan.md
README.md
project_plan.md
research_log.md
requirements.txt
.gitignore
```

## Limitations

This project does not establish causality. It relies on public market data, simplified hedging classifications, and a small sample of four airlines. Results should be interpreted as exploratory rather than definitive.
