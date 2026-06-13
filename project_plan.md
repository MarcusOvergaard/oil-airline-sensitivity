# Project Plan

## Project Title

Fuel, Hedging, and Business Models: An Analysis of Airline Stock Sensitivity to Oil Price Changes

---

# Project Objective

Build a portfolio-quality data analysis project that investigates whether different airline business models exhibit different sensitivities to oil price movements.

The project should serve two purposes:

1. Demonstrate data analysis skills using Python and Tableau.
2. Generate potentially useful investing insights.

The project is exploratory and does not attempt to prove a predetermined conclusion.

---

# Main Research Question

How sensitive are different airline business models to changes in oil prices?

---

# Success Criteria

The project is successful if it can answer:

1. Which airline exhibits the highest sensitivity to oil price changes?
2. Which airline exhibits the lowest sensitivity to oil price changes?
3. Do airlines with historically stronger fuel hedging programs appear less sensitive to oil price changes?
4. Do low-cost carriers appear less sensitive than legacy carriers?
5. Are results consistent between weekly and monthly return periods?
6. Do airline stocks react to oil price movements as strongly as many investors assume?

Success does NOT require proving any particular hypothesis.

---

# Hypotheses

## H1

Airline stocks may react negatively to oil price increases.

## H2

Low-cost carriers may show different oil sensitivities than legacy carriers.

## H3

Airlines with historically stronger hedging programs may show lower sensitivity to oil price increases.

## H4

Results may differ between weekly and monthly return periods.

---

# Assets

## Oil Benchmark

Brent Crude Oil Futures

Ticker:

BZ=F

---

## Airlines

### Ryanair

Ticker:

RYAAY

Classification:

* Region: Europe
* Business Model: Low-Cost
* Hedging Profile: Historically Higher Hedging

### Lufthansa

Ticker:

LHA.DE

Classification:

* Region: Europe
* Business Model: Legacy
* Hedging Profile: Mixed / Moderate Hedging

### Southwest Airlines

Ticker:

LUV

Classification:

* Region: United States
* Business Model: Low-Cost
* Hedging Profile: Historically Strong Hedging

### American Airlines

Ticker:

AAL

Classification:

* Region: United States
* Business Model: Legacy
* Hedging Profile: Historically Lower Hedging

---

## Market Benchmark

S&P 500

Ticker:

^GSPC

---

# Time Period

Start Date:

2018-01-01

End Date:

Latest Available

---

# Frequencies

Use both:

* Weekly returns
* Monthly returns

Weekly returns provide more observations.

Monthly returns provide lower-noise investment-oriented analysis.

Monthly results should be considered the primary interpretation layer.

Weekly results should be used as a robustness check.

---

# Excess Return Definition

For each airline:

Excess Return = Airline Return − S&P500 Return

Purpose:

Measure performance relative to the overall market.

---

# Data Sources

Primary Source:

Yahoo Finance via yfinance

---

# Required Python Libraries

pandas

numpy

yfinance

matplotlib

seaborn

scipy

statsmodels

jupyter

---

# Repository Structure

oil-airline-sensitivity/

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

---

# Dataset Outputs

## Raw Data

data/raw/raw_prices.csv

---

## Processed Data

data/processed/weekly_returns.csv

data/processed/monthly_returns.csv

data/processed/weekly_excess_returns.csv

data/processed/monthly_excess_returns.csv

---

## Tableau Dataset

data/tableau/airline_oil_tableau_dataset.csv

Required columns:

date

frequency

asset

asset_type

region

business_model

hedging_profile

return

sp500_return

excess_return

brent_return

---

# Analysis Requirements

## Normalized Performance

Create normalized price series starting at 100.

Purpose:

Compare long-term performance.

---

## Correlation Analysis

Perform:

* Weekly correlation matrix
* Monthly correlation matrix

Purpose:

Identify relationships among oil, airlines, and market benchmark.

---

## Oil Sensitivity Analysis

Estimate:

airline_return = alpha + beta × brent_return

Calculate:

* alpha
* beta
* r_squared
* p_value

For:

* Weekly returns
* Monthly returns
* Excess returns

Output:

data/processed/oil_sensitivity_summary.csv

---

## Oil Shock Analysis

Define oil shock periods as the top 20% of positive Brent returns.

Calculate:

Average airline return during oil shock periods.

Output:

data/processed/oil_shock_summary.csv

---

# Tableau Dashboard Goals

Dashboard 1:

Normalized Performance Comparison

Question:

Which assets performed best over time?

---

Dashboard 2:

Weekly vs Monthly Correlation Comparison

Question:

Which assets move together?

---

Dashboard 3:

Oil Sensitivity Ranking

Question:

Which airlines appear most sensitive to oil price changes?

---

Dashboard 4:

Oil Shock Analysis

Question:

How do airlines behave during major oil increases?

---

Dashboard 5:

Excess Return Comparison

Question:

Which airlines outperformed or underperformed the market?

---

Dashboard 6:

Business Model Comparison

Question:

Do low-cost and legacy carriers exhibit different behavior?

---

# Limitations

This project does not establish causality.

The project relies on publicly available market data.

Hedging profiles are simplified classifications and may change through time.

The sample size is limited to four airlines.

Results should be interpreted as exploratory rather than definitive.

---

# Execution Rules For Hermes

Work sequentially.

Complete one phase at a time.

Validate outputs before continuing.

Never skip validation steps.

Report errors immediately.

Stop after each phase and wait for confirmation before moving to the next phase.

---

# Phase Order

Phase 1

Create repository structure and files.

Stop.

---

Phase 2

Create Notebook 01 and download data.

Validate data.

Stop.

---

Phase 3

Create Notebook 02 and calculate returns.

Validate outputs.

Stop.

---

Phase 4

Create Notebook 03 and perform analysis.

Validate outputs.

Stop.

---

Phase 5

Create Notebook 04 and validate Tableau dataset.

Stop.

---

Phase 6

Prepare Tableau assets and documentation.

Stop.

---

Phase 7

Finalize README and GitHub presentation materials.

Stop.
