# Tableau Export Validation Report

- Generated: 2026-06-13 17:56:57
- Validation status: **READY FOR TABLEAU**

## Row Counts

- data/tableau/airline_oil_tableau_dataset.csv: 2164 rows
- data/processed/oil_sensitivity_summary.csv: 16 rows
- data/processed/oil_shock_summary.csv: 8 rows
- data/processed/oil_market_sensitivity_summary.csv: 8 rows

## Dataset Checks

### Tableau Dataset

- Path: `data/tableau/airline_oil_tableau_dataset.csv`
- Validation status: **PASS**
- File exists: True
- Row count: 2164
- Column count: 11
- Required columns present: True
- Missing required columns: []
- Missing-value total: 0
- Missing values by column:
  - None
- Frequency values: ['Monthly', 'Weekly']
- Missing frequencies: []
- Extra frequencies: []
- Airline coverage: ['American Airlines', 'Lufthansa', 'Ryanair', 'Southwest']
- Missing airlines: []
- Extra airlines: []
- Numeric type checks:
  - return: numeric
  - excess_return: numeric
  - brent_return: numeric
  - sp500_return: numeric
- Business model / region / hedging profile population checks:
  - business_model: populated
  - region: populated
  - hedging_profile: populated
- Date parse failures: 0
- Date range: 2018-01-12 to 2026-06-30

### Oil Sensitivity Summary

- Path: `data/processed/oil_sensitivity_summary.csv`
- Validation status: **PASS**
- File exists: True
- Row count: 16
- Column count: 11
- Required columns present: True
- Missing required columns: []
- Missing-value total: 0
- Missing values by column:
  - None
- Frequency values: ['Monthly', 'Weekly']
- Missing frequencies: []
- Extra frequencies: []
- Airline coverage: ['American Airlines', 'Lufthansa', 'Ryanair', 'Southwest']
- Missing airlines: []
- Extra airlines: []
- Numeric type checks:
  - alpha: numeric
  - beta: numeric
  - r_squared: numeric
  - p_value: numeric
  - beta_rank: numeric
  - beta_confidence_score: numeric
- Return type values: ['Excess Returns', 'Returns']
- Contains return analysis: True
- Contains excess return analysis: True

### Oil Shock Summary

- Path: `data/processed/oil_shock_summary.csv`
- Validation status: **PASS**
- File exists: True
- Row count: 8
- Column count: 5
- Required columns present: True
- Missing required columns: []
- Missing-value total: 0
- Missing values by column:
  - None
- Frequency values: ['Monthly', 'Weekly']
- Missing frequencies: []
- Extra frequencies: []
- Airline coverage: ['American Airlines', 'Lufthansa', 'Ryanair', 'Southwest']
- Missing airlines: []
- Extra airlines: []
- Numeric type checks:
  - oil_shock_count: numeric
  - average_return_during_oil_shocks: numeric
  - average_excess_return_during_oil_shocks: numeric
- Oil shock count range: 12 to 48
- Non-positive oil shock counts: 0

### Market Controlled Sensitivity Summary

- Path: `data/processed/oil_market_sensitivity_summary.csv`
- Validation status: **PASS**
- File exists: True
- Row count: 8
- Column count: 11
- Required columns present: True
- Missing required columns: []
- Missing-value total: 0
- Missing values by column:
  - None
- Frequency values: ['Monthly', 'Weekly']
- Missing frequencies: []
- Extra frequencies: []
- Airline coverage: ['American Airlines', 'Lufthansa', 'Ryanair', 'Southwest']
- Missing airlines: []
- Extra airlines: []
- Numeric type checks:
  - oil_beta: numeric
  - market_beta: numeric
  - oil_p_value: numeric
  - market_p_value: numeric
  - r_squared: numeric
- Significant-flag checks:
  - oil_significant: values=['False', 'True'], invalid_values=[]
  - market_significant: values=['True'], invalid_values=[]

## Warnings and Limitations

- The validation confirms schema, completeness, coverage, and basic type integrity; it does not re-run the underlying analytical regressions.
- Hedging profiles are simplified static labels and should be interpreted as exploratory classifications.
- Monthly analysis remains the primary interpretation layer; weekly analysis is a robustness check.

## Final Readiness Status

**READY FOR TABLEAU**

All required Tableau export and summary files passed validation and are ready for dashboard building.