# Fuel, Hedging, and Business Models: Airline Stock Sensitivity to Oil

**A Python and Tableau portfolio project exploring how sensitive airline stocks are to oil prices and the broader stock market.**

Interactive Tableau dashboards: [(https://public.tableau.com/app/profile/marcus.timm/vizzes)]

## Project Overview

This project investigates whether airline stocks are driven more by Brent crude oil prices or by the broader equity market.

## Tools Used

- Python
- pandas
- NumPy
- yfinance
- scipy
- statsmodels
- matplotlib
- seaborn
- Jupyter Notebook
- Tableau
- Git / GitHub

## Skills Demonstrated

- Financial data collection with Python
- Data cleaning and transformation using pandas
- Time-series return analysis
- Linear regression and statistical interpretation
- Market-adjusted performance analysis
- Financial data visualization with Matplotlib
- Interactive dashboard development with Tableau
- Data validation and quality assurance
- Git version control and technical documentation

## Dataset

Historical daily price data was downloaded from Yahoo Finance using the `yfinance` library.

Period: 2018-01-01 to latest available.

Assets analyzed:

- Brent Crude Oil
- S&P 500
- Ryanair
- Lufthansa
- Southwest Airlines
- American Airlines

## Methodology

1. Download historical prices from Yahoo Finance.
2. Calculate weekly and monthly returns.
3. Compute airline excess returns relative to the S&P 500.
4. Estimate simple and market-controlled regression models.
5. Analyze airline performance during oil shock periods.
6. Visualize and validate the results using Python and Tableau.

## Project Workflow

Raw Market Data
↓
Weekly & Monthly Returns
↓
Excess Returns
↓
Regression Analysis
↓
Market-Controlled Models
↓
Tableau Dashboard & Final Findings

## Visual Findings

### Normalized Performance

![Normalized performance](images/normalized_performance.png)

**What this shows**

Brent experienced large price swings, but airline performance differed across companies. This suggests that factors beyond oil prices influence long-term airline returns.

---

### Monthly Correlation Matrix

![Monthly correlation heatmap](images/monthly_correlation_heatmap.png)

**What this shows**

Airline stocks are more closely correlated with each other and with the S&P 500 than with Brent oil. This suggests oil alone explains little of their return variation.

---

### Weekly Correlation Matrix

![Weekly correlation heatmap](images/weekly_correlation_heatmap.png)

**What this shows**

Weekly relationships between Brent and airline returns are even weaker than the monthly results, suggesting short-term movements are dominated by market noise.

---

### Market-Controlled Oil Beta Ranking

![Market-controlled oil beta ranking](images/market_controlled_oil_beta_ranking.png)

**What this shows**

After controlling for market movements, none of the airlines has a statistically significant monthly oil beta. Market exposure explains airline returns much better than oil prices.

---

### Market Exposure vs. Oil Exposure

![Market Exposure vs. Oil Exposure](images/market_exposure_vs_oil_exposure.png)

**What this shows**

All four airlines have much larger market betas than oil betas, reinforcing that the broader market has a greater influence than oil prices.

---

## Tableau Dashboards

### Dashboard 1 — Project Overview

![Dashboard 1](images/tableau_dashboard_overview.png)

A summary of the airlines, business models, regions, and hedging classifications.

---

### Dashboard 2 — Market-Controlled Regression Results

![Dashboard 2](images/tableau_dashboard_market_controlled.png)

A comparison of market beta and oil beta for each airline.

## Key Findings

- Market exposure dominates oil exposure after controlling for the S&P 500.
- Monthly oil beta is not statistically significant for any airline in the market-controlled model.
- Market beta is statistically significant for all airlines and substantially larger than oil beta.
- Weekly oil sensitivity remains significant only for Ryanair and American Airlines.
- The common assumption that airline stocks are primarily driven by oil prices is not supported by the data.

## Final Conclusion

Airline stock returns appear to be driven far more by broad market movements than by Brent crude oil prices. Although the initial analysis suggested some oil sensitivity, those relationships largely disappeared after controlling for market performance.

## Limitations

- This is exploratory analysis, not causal proof.
- Regression relationships are historical associations only.
- Several oil-only models have low R² values, meaning Brent returns explain only a small share of airline return variation.
- Hedging classifications are simplified and may not reflect each airline’s exact hedge book through time.
- The sample is limited to four airlines.
- Weekly results are noisier than monthly results.

## How to Run

```bash
pip install -r requirements.txt
jupyter notebook
```
Run the notebooks in numerical order (`01` → `04`).

## Disclaimer

This project was created for educational and portfolio purposes and should not be considered investment advice.

---

