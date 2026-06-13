# Tableau Dashboard Plan

The Tableau dashboard will present the project findings after the Python analysis is complete.

## Planned Dashboards

1. Normalized Performance Comparison
   - Compare Brent oil, selected airlines, and the S&P 500 from a common starting value.

2. Weekly vs Monthly Correlation Comparison
   - Show whether relationships differ by return frequency.

3. Oil Sensitivity Ranking
   - Rank airlines by estimated beta to Brent returns.

4. Oil Shock Analysis
   - Compare average airline returns during the top 20% of positive Brent-return periods.

5. Excess Return Comparison
   - Compare airline performance relative to the S&P 500.

6. Business Model Comparison
   - Compare low-cost and legacy carriers using the final processed dataset.

## Tableau Dataset

Expected file:

`data/tableau/airline_oil_tableau_dataset.csv`

Required columns:

- date
- frequency
- asset
- asset_type
- region
- business_model
- hedging_profile
- return
- sp500_return
- excess_return
- brent_return
