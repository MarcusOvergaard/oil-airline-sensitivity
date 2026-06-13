# Key Findings

## Main Conclusions

1. Market exposure dominates oil exposure after controlling for the S&P 500.
2. Monthly oil beta is not statistically significant for any of the four airlines in the market-controlled model.
3. Market beta is statistically significant for all airlines across both weekly and monthly frequencies.
4. Weekly oil beta remains statistically significant only for Ryanair and American Airlines, and both relationships are negative.
5. Simple oil sensitivity is weak and inconsistent.
6. The original “oil hurts airlines” assumption is too simplistic.

## Strongest Evidence

### Market-controlled regression

The market-controlled model is the most important evidence source because it separates Brent-return exposure from broad equity-market exposure.

Key results:

- Monthly oil beta is not significant for Ryanair, Lufthansa, Southwest, or American Airlines.
- Market beta is significant for all four airlines at both weekly and monthly frequencies.
- Market beta is larger than oil beta in absolute terms in every market-controlled row.
- Weekly oil beta remains significant only for:
  - American Airlines: oil beta `-0.118`, oil p-value `0.040`, market beta `1.795`, R² `0.305`.
  - Ryanair: oil beta `-0.099`, oil p-value `0.010`, market beta `1.146`, R² `0.283`.

### Simple oil sensitivity

The simple oil model produced only two statistically significant relationships:

- Ryanair monthly returns: beta `0.177`, p-value `0.031`, R² `0.046`.
- Ryanair weekly excess returns: beta `-0.085`, p-value `0.024`, R² `0.012`.

Both have low explanatory power, so the simple model should be interpreted cautiously.

### Oil shock analysis

Oil-shock results depend heavily on frequency.

Monthly average excess returns during oil shocks:

1. Southwest: `1.98%`
2. Lufthansa: `1.60%`
3. Ryanair: `0.85%`
4. American Airlines: `-0.69%`

Weekly average excess returns during oil shocks were negative for all four airlines.

## What Surprised Us

- Ryanair’s simple monthly oil beta was positive and statistically significant, which runs against the basic assumption that rising oil prices should mechanically hurt airlines.
- That Ryanair result weakened after controlling for the S&P 500, suggesting the simple relationship was likely driven by broader market co-movement rather than oil-specific exposure.
- Market beta was consistently significant across all airlines and frequencies.
- Oil shock results were not uniformly negative, especially at the monthly frequency.

## Limitations

- Correlation is not causation.
- Low R² values limit the strength of several oil-only conclusions.
- Hedging classifications are simplified historical labels, not detailed hedge-book data.
- The sample includes only four airlines.
- Weekly data provides more observations but is noisier than monthly data.
- Public market data can reflect trading-calendar differences, regional exchange holidays, and ticker-specific availability.
- The analysis does not include fuel expense ratios, route mix, balance sheet structure, pricing power, labor costs, or real-time hedging positions.

## What Could Be Improved Later

- Add more airlines across more regions.
- Include direct fuel-cost exposure from company filings.
- Add time-varying hedging data if available.
- Test additional market benchmarks, such as regional equity indexes.
- Split analysis into pre-COVID, COVID, and post-COVID regimes.
- Compare Brent with jet fuel crack spreads or other aviation-specific fuel proxies.
- Add rolling regression windows to test whether oil sensitivity changes over time.
