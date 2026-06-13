# Data Dictionary

This file summarizes the main datasets created by the project.

## `data/raw/raw_prices.csv`

Raw adjusted close price data downloaded from Yahoo Finance via `yfinance`.

Main fields:

- `Date`: Trading date.
- `Brent Oil`: Brent crude oil futures price proxy.
- `Ryanair`: Ryanair adjusted close price.
- `Lufthansa`: Lufthansa adjusted close price.
- `Southwest`: Southwest Airlines adjusted close price.
- `American Airlines`: American Airlines adjusted close price.
- `S&P 500`: S&P 500 adjusted close price.

Notes:

- Raw data may contain missing values because assets trade on different calendars and exchanges.
- Missing values are reported in the project log rather than blindly filled at the raw-data stage.

## `data/processed/weekly_returns.csv`

Weekly return series calculated from period-end prices.

Main fields:

- `Date`: Weekly period-end date.
- Asset return columns for Brent Oil, the four airlines, and the S&P 500.

Purpose:

- Provides higher-observation return data for robustness checks and weekly regression analysis.

## `data/processed/monthly_returns.csv`

Monthly return series calculated from period-end prices.

Main fields:

- `Date`: Monthly period-end date.
- Asset return columns for Brent Oil, the four airlines, and the S&P 500.

Purpose:

- Provides the primary investment-oriented return frequency for interpretation.

## `data/processed/weekly_excess_returns.csv`

Weekly airline excess returns relative to the S&P 500.

Definition:

`Excess Return = Airline Return - S&P 500 Return`

Main fields:

- `Date`: Weekly period-end date.
- One excess-return column for each airline.

Purpose:

- Shows airline performance after subtracting broad market movement.

## `data/processed/monthly_excess_returns.csv`

Monthly airline excess returns relative to the S&P 500.

Definition:

`Excess Return = Airline Return - S&P 500 Return`

Main fields:

- `Date`: Monthly period-end date.
- One excess-return column for each airline.

Purpose:

- Provides monthly market-relative performance for the main interpretation layer.

## `data/tableau/airline_oil_tableau_dataset.csv`

Validated Tableau-ready long-format dataset with airline rows only.

Main fields:

- `date`: Period-end date.
- `frequency`: Weekly or Monthly.
- `asset`: Airline name.
- `asset_type`: Asset category.
- `region`: Europe or United States.
- `business_model`: Low-Cost or Legacy.
- `hedging_profile`: Simplified historical hedging classification.
- `return`: Airline return.
- `sp500_return`: S&P 500 return for the same period.
- `excess_return`: Airline return minus S&P 500 return.
- `brent_return`: Brent crude oil futures return for the same period.

Purpose:

- Main input for Tableau dashboards.

## `data/processed/oil_sensitivity_summary.csv`

Simple oil-sensitivity regression results.

Model:

`Airline Return = alpha + beta * Brent Return`

Main fields:

- `airline`: Airline name.
- `frequency`: Weekly or Monthly.
- `return_type`: Returns or Excess Returns.
- `alpha`: Regression intercept.
- `beta`: Estimated Brent-return sensitivity.
- `r_squared`: Share of variation explained by the model.
- `p_value`: Statistical significance of the Brent beta.
- `interpretation`: Plain-English beta interpretation.
- `beta_rank`: Rank by absolute beta within the relevant group.
- `significant`: Whether the Brent beta is statistically significant.
- `beta_confidence_score`: Combined strength indicator based on beta, significance, and explanatory power.

## `data/processed/oil_market_sensitivity_summary.csv`

Market-controlled oil-sensitivity regression results.

Model:

`Airline Return = alpha + oil_beta * Brent Return + market_beta * S&P 500 Return`

Main fields:

- `airline`: Airline name.
- `frequency`: Weekly or Monthly.
- `alpha`: Regression intercept.
- `oil_beta`: Brent-return sensitivity after controlling for the S&P 500.
- `oil_p_value`: Statistical significance of oil beta.
- `market_beta`: S&P 500 return sensitivity.
- `market_p_value`: Statistical significance of market beta.
- `r_squared`: Share of airline return variation explained by oil and market returns together.
- `oil_significant`: Whether oil beta is statistically significant.
- `market_significant`: Whether market beta is statistically significant.
- `interpretation`: Plain-English model interpretation.

Purpose:

- Main evidence source for the project’s final conclusion that market exposure dominates oil exposure.

## `data/processed/oil_shock_summary.csv`

Average airline behavior during oil-shock periods.

Definition:

- Oil shocks are the top 20% of positive Brent-return periods for each frequency.

Main fields:

- `airline`: Airline name.
- `frequency`: Weekly or Monthly.
- `oil_shock_count`: Number of oil-shock periods.
- `average_return_during_oil_shocks`: Average airline return during oil-shock periods.
- `average_excess_return_during_oil_shocks`: Average airline excess return during oil-shock periods.

Purpose:

- Complements regression analysis with a stress-period view of airline performance during large positive oil moves.
