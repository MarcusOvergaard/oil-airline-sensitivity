# Fuel, Hedging, and Business Models: Airline Stock Sensitivity to Oil

**A Python and Tableau portfolio project investigating whether airline stocks are driven more by Brent crude oil prices or by the broader equity market.**

Interactive Tableau dashboards: [(https://public.tableau.com/app/profile/marcus.timm/vizzes)]

## Research Question

How sensitive are different airline business models to changes in oil prices?

## Why This Project Matters

Fuel is one of the most visible costs in the airline industry, so it is tempting to assume that rising oil prices automatically hurt airline stocks. This project tests that assumption using market data, weekly and monthly returns, excess returns versus the S&P 500, oil-shock periods, and market-controlled regression models.

The result is more nuanced: oil matters in some cases, but broad equity-market exposure explains much more of the observed airline stock movement.

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

## Dataset

Historical daily price data was collected from Yahoo Finance using the `yfinance` library.

Period:
2018-01-01 to latest available.

Assets:

| Asset | Ticker |
|--------|--------|
| Brent Crude Oil | BZ=F |
| S&P 500 | ^GSPC |
| Ryanair | RYAAY |
| Lufthansa | LHA.DE |
| Southwest Airlines | LUV |
| American Airlines | AAL |

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
Market-Controlled Regression
↓
Tableau Dashboard & Final Findings

## Visual Findings

### Normalized Performance

![Normalized performance](images/normalized_performance.png)

**What this shows**

This chart compares the cumulative performance of Brent crude oil, the four airline stocks, and the S&P 500 using a common starting value of 100. Although Brent experienced substantial price swings throughout the sample period, airline performance varied considerably across companies. This suggests that factors beyond oil prices play an important role in determining long-term airline stock returns.

---

### Monthly Correlation Matrix

![Monthly correlation heatmap](images/monthly_correlation_heatmap.png)

**What this shows**

Monthly correlations reveal that airline stocks are much more closely correlated with one another and with the S&P 500 than with Brent oil. Brent exhibits only weak positive correlations with the airlines, providing an early indication that oil alone explains little of their return variation.

---

### Weekly Correlation Matrix

![Weekly correlation heatmap](images/weekly_correlation_heatmap.png)

**What this shows**

Weekly correlations between Brent and airline returns are even weaker than the monthly relationships. Short-term price movements appear dominated by market noise, while relationships among airline stocks remain comparatively stronger.

---

### Market-Controlled Oil Beta Ranking

![Market-controlled oil beta ranking](images/market_controlled_oil_beta_ranking.png)

**What this shows**

After controlling for overall market movements, none of the airlines exhibits a statistically significant monthly oil beta. This supports the project's central finding that broad market exposure explains airline returns much better than Brent crude oil prices.

---

### Market Exposure vs. Oil Exposure

![Market Exposure vs. Oil Exposure](images/market_exposure_vs_oil_exposure.png)

**What this shows**

This scatter plot directly compares each airline's market beta with its oil beta. All four airlines exhibit market betas substantially larger than their oil betas, visually reinforcing the conclusion that overall equity-market movements have a much greater influence on airline stock returns than oil prices.

---

## Tableau Dashboards

In addition to the Python analysis, two interactive Tableau dashboards were created to summarize the project and communicate the regression results.

### Dashboard 1 — Project Overview

![Dashboard 1](images/tableau_dashboard_overview.png)

Provides an overview of the project, including the airlines analyzed, their business models, regions, and historical hedging classifications.

---

### Dashboard 2 — Market-Controlled Regression Results

![Dashboard 2](images/tableau_dashboard_market_controlled.png)

This dashboard summarizes the market-controlled regression analysis, comparing each airline's oil beta with its market beta after controlling for overall equity market movements. It serves as the primary Tableau visualization supporting the project's main conclusion.

## Key Findings

- Market exposure dominates oil exposure after controlling for the S&P 500.
- Monthly oil beta is not statistically significant for any airline in the market-controlled model.
- Market beta is statistically significant for all airlines and substantially larger than oil beta.
- Weekly oil sensitivity remains significant only for Ryanair and American Airlines.
- The common assumption that airline stocks are primarily driven by oil prices is not supported by the data.

## Final Conclusion

Airline stock returns appear to be driven far more by broad market movements than by Brent crude oil prices. While simple regressions initially suggested some oil sensitivity, these relationships largely disappeared after controlling for overall market performance.

## Limitations

- This is exploratory analysis, not causal proof.
- Regression relationships are historical associations only.
- Several oil-only models have low R² values, meaning Brent returns explain only a small share of airline return variation.
- Hedging classifications are simplified and may not reflect each airline’s exact hedge book through time.
- The sample is limited to four airlines.
- Weekly results are noisier than monthly results.

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

## How to Run

````markdown
```bash
pip install -r requirements.txt
jupyter notebook

- Run the notebooks in numerical order (01 → 04).

## Disclaimer

This project was created for educational and portfolio purposes. The analysis is exploratory and should not be considered investment advice.

