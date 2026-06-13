# Tableau Dashboard Plan

This Tableau story should be built around the actual project findings, not around the original hypotheses. The central message is that simple oil sensitivity looks weak and inconsistent, and once market exposure is controlled for, broad equity-market movement explains airline returns much more than Brent oil returns.

Do not build dashboards until the Tableau workbook phase begins. This file is the design specification only.

## Data Sources

Use the validated Phase 5 files:

- `data/tableau/airline_oil_tableau_dataset.csv`
- `data/processed/oil_sensitivity_summary.csv`
- `data/processed/oil_shock_summary.csv`
- `data/processed/oil_market_sensitivity_summary.csv`
- `data/processed/tableau_validation_report.md` as the validation reference

Validation status from Phase 5: ready for Tableau.

Row counts:

- Tableau dataset: 2,164 rows
- Oil sensitivity summary: 16 rows
- Oil shock summary: 8 rows
- Market-controlled sensitivity summary: 8 rows

## Story Structure

Recommended title:

**Do Airline Stocks Really Move With Oil? A Market-Controlled View**

Recommended narrative arc:

1. Start with project scope and dataset readiness.
2. Show the simple oil sensitivity results.
3. Show why the market-controlled model changes the interpretation.
4. Show what happens during oil shock periods.
5. End with final findings and caveats.

## Dashboard 1: Project Overview

### Purpose

Introduce the research question, the four airlines, the classification framework, and the validated Tableau dataset. This dashboard should orient the reader before showing regression outputs.

### Charts

- KPI cards:
  - Date range: 2018-01-12 to 2026-06-30
  - Tableau dataset rows: 2,164
  - Airlines: 4
  - Frequencies: Weekly and Monthly
  - Validation status: Ready for Tableau
- Airline classification table:
  - Airline
  - Region
  - Business model
  - Hedging profile
- Optional line chart:
  - Average or indexed return path by airline from the Tableau dataset, filtered to Monthly by default.

### Filters

- Frequency: Weekly / Monthly
- Airline
- Region
- Business model
- Hedging profile

### Key Metrics

- Row count
- Airline count
- Frequency count
- Date range
- Validation status

### User Questions Answered

- What companies are included?
- What period does the dataset cover?
- Are the Tableau inputs clean and complete?
- Which classifications are used for business model and hedging profile?

## Dashboard 2: Simple Oil Sensitivity

### Purpose

Show the first-pass relationship between Brent returns and airline returns before controlling for the broader equity market. This dashboard should make clear that the simple relationship is weak and inconsistent.

### Charts

- Bar chart: simple Brent beta by airline
  - Split or toggle by frequency and return type.
  - Use color for significance.
- Scatter plot: airline return vs Brent return
  - One airline at a time, with trend line.
  - Tooltip should show beta, p-value, and R².
- Table: simple regression summary
  - Airline
  - Frequency
  - Return type
  - Beta
  - P-value
  - R²
  - Significant
  - Beta rank
  - Beta confidence score

### Filters

- Frequency: Weekly / Monthly
- Return type: Returns / Excess Returns
- Airline
- Significant only: True / False
- Business model
- Hedging profile

### Key Metrics

- Beta
- P-value
- R²
- Significant flag
- Beta rank
- Beta confidence score

### User Questions Answered

- Which airline appears most sensitive to Brent returns in the simple model?
- Are simple oil relationships statistically significant?
- Are results consistent between weekly and monthly returns?
- Does excess-return analysis tell a different story from raw-return analysis?

### Findings To Surface

- Simple significant relationships are limited:
  - Ryanair monthly returns: beta 0.177, p-value 0.031, R² 0.046.
  - Ryanair weekly excess returns: beta -0.085, p-value 0.024, R² 0.012.
- Even statistically significant simple relationships have low explanatory power.
- Monthly simple return betas are positive for all four airlines, which is counterintuitive if the expected story is simply “higher oil hurts airlines.”

## Dashboard 3: Market-Controlled Sensitivity

### Purpose

Make this the analytical centerpiece. It should show that once S&P 500 returns are included, oil sensitivity largely disappears at the monthly level and market beta dominates across all airlines.

### Charts

- Side-by-side bar chart:
  - Oil beta vs market beta by airline.
  - Separate panes for Weekly and Monthly.
- Highlight table:
  - Airline
  - Frequency
  - Oil beta
  - Oil p-value
  - Market beta
  - Market p-value
  - R²
  - Oil significant
  - Market significant
- Scatter or dot plot:
  - X-axis: oil beta
  - Y-axis: market beta
  - Color: oil significant
  - Shape: frequency
- Optional annotation card:
  - “Monthly oil sensitivity was not significant for any airline after market control.”

### Filters

- Frequency: Weekly / Monthly
- Airline
- Oil significant: True / False
- Market significant: True / False
- Business model
- Region

### Key Metrics

- Oil beta
- Oil p-value
- Market beta
- Market p-value
- R²
- Oil significant flag
- Market significant flag

### User Questions Answered

- Does oil still matter after controlling for the S&P 500?
- Is the broader market more important than Brent oil returns?
- Which airlines have statistically significant oil exposure after market control?
- Are monthly and weekly conclusions different?

### Findings To Surface

- Monthly oil beta is not statistically significant for any airline after market control.
- Market beta is statistically significant for every airline and both frequencies.
- Market beta is larger than oil beta in absolute terms in every row.
- Weekly oil beta remains significant only for:
  - American Airlines: oil beta -0.118, oil p-value 0.040, market beta 1.795, R² 0.305.
  - Ryanair: oil beta -0.099, oil p-value 0.010, market beta 1.146, R² 0.283.
- Ryanair’s positive monthly simple oil beta weakens after market control, suggesting the simple result was likely market-driven rather than oil-specific.

## Dashboard 4: Oil Shock Analysis

### Purpose

Show how airlines behaved during the top 20% of positive Brent-return periods. This gives a more intuitive “stress period” view than regression alone.

### Charts

- Bar chart: average return during oil shock periods by airline.
- Bar chart: average excess return during oil shock periods by airline.
- Small multiples:
  - Monthly shock results
  - Weekly shock results
- Table:
  - Airline
  - Frequency
  - Oil shock count
  - Average return during oil shocks
  - Average excess return during oil shocks

### Filters

- Frequency: Weekly / Monthly
- Airline
- Business model
- Region
- Hedging profile

### Key Metrics

- Oil shock count
- Average return during oil shocks
- Average excess return during oil shocks

### User Questions Answered

- What happened during large positive Brent-return periods?
- Which airlines performed best or worst during oil shocks?
- Were oil shock results better or worse relative to the S&P 500?
- Do monthly and weekly shock results tell the same story?

### Findings To Surface

- Monthly oil shock periods: Southwest had the highest average excess return, followed by Lufthansa, Ryanair, and American Airlines.
- Monthly oil shock average excess returns:
  - Southwest: 1.98%
  - Lufthansa: 1.60%
  - Ryanair: 0.85%
  - American Airlines: -0.69%
- Weekly oil shock excess returns were negative for all four airlines.
- Oil shock interpretation depends strongly on frequency.

## Dashboard 5: Final Findings

### Purpose

Summarize the final investment and methodology conclusions. This should be the executive summary dashboard and should explicitly prevent overclaiming.

### Charts

- Finding cards:
  - “Market exposure dominates oil exposure.”
  - “Monthly oil sensitivity is not significant after market control.”
  - “Weekly oil sensitivity remains for Ryanair and American Airlines only.”
  - “Oil shock results vary by frequency.”
- Compact comparison table:
  - Airline
  - Business model
  - Hedging profile
  - Monthly market-controlled oil beta
  - Monthly oil p-value
  - Weekly market-controlled oil beta
  - Weekly oil p-value
  - Monthly oil shock excess return
- Optional final ranking:
  - “Most notable oil-sensitive cases after market control” limited to the two significant weekly rows.

### Filters

- Airline
- Business model
- Hedging profile
- Region

### Key Metrics

- Monthly oil beta
- Weekly oil beta
- Oil p-value
- Market beta
- R²
- Oil shock excess return

### User Questions Answered

- What is the main conclusion?
- Which result should an investor pay most attention to?
- Did the original oil-sensitivity hypothesis survive market control?
- What should not be inferred from this analysis?

## Key Findings To Highlight

1. The market-controlled model is more decision-useful than the simple oil model.
2. Monthly oil sensitivity is not statistically significant for any airline after controlling for the S&P 500.
3. Market beta is significant for every airline and both frequencies.
4. Market beta is larger than oil beta in absolute terms in every market-controlled row.
5. Weekly oil sensitivity remains significant only for Ryanair and American Airlines, and both relationships are negative.
6. Simple oil sensitivity is weak and inconsistent; the strongest simple findings still have low R² values.
7. Ryanair’s positive monthly simple oil beta likely reflects broader market co-movement rather than clean oil-specific exposure.
8. Oil shock results are frequency-dependent: monthly shock excess returns are positive for Southwest, Lufthansa, and Ryanair, but weekly shock excess returns are negative for all four airlines.
9. The project is exploratory, not causal.

## Potential Misinterpretations To Avoid

- Correlation is not causation. Regression coefficients show historical associations, not proof that oil price moves caused airline stock moves.
- Low R² values matter. Many oil-only relationships explain very little of airline return variation, even when a p-value is below 0.05.
- Simplified hedging classifications are not live operational hedging data. They are broad labels for exploratory comparison.
- The airline sample is limited to four companies. Do not generalize too aggressively to the entire airline industry.
- Weekly findings should not override the monthly interpretation layer. Weekly data offers more observations, but it is noisier.
- Positive simple oil betas should not be read as “oil helps airlines” without market control.
- Oil shock averages describe selected historical periods; they are not forecasts.
- The Tableau validation confirms file quality and schema readiness, not the economic truth of the model.

## Recommended Tableau Build Order

1. Connect to the validated Tableau dataset first:
   - `data/tableau/airline_oil_tableau_dataset.csv`
2. Add the three summary CSVs as separate data sources:
   - `data/processed/oil_sensitivity_summary.csv`
   - `data/processed/oil_market_sensitivity_summary.csv`
   - `data/processed/oil_shock_summary.csv`
3. Build Dashboard 1 first to establish project scope, filters, and visual style.
4. Build Dashboard 3 second because it contains the main finding and should guide the story.
5. Build Dashboard 2 third as the “before market control” comparison.
6. Build Dashboard 4 fourth to add the oil-shock stress-period view.
7. Build Dashboard 5 last as the executive summary after the supporting dashboards are stable.
8. Add tooltips and annotations only after the charts are correct.
9. Cross-check dashboard row counts and filter behavior against `data/processed/tableau_validation_report.md`.
10. Avoid adding new analysis inside Tableau that was not already produced in Python, unless explicitly documented later.

## Design Notes

- Use Monthly as the default frequency where a choice is required.
- Use Weekly as a robustness-check toggle, not the headline view.
- Use consistent colors:
  - Brent/oil metrics: dark orange or brown
  - Market metrics: blue
  - Airlines: stable categorical palette
  - Significant results: stronger saturation or icon marker
- Include p-values and R² in tooltips for every regression chart.
- Put cautionary text near charts with statistically significant but low-R² results.
- Keep the final story restrained: the best conclusion is “oil is less dominant than assumed,” not “oil does not matter.”
