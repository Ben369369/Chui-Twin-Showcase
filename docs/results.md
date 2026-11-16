# Results

## 1. Sealed live forecasts (Q3 2026)

Each forecast was hashed and timestamped in Bitcoin before the company reported. An outcome was accepted only
if it became public after the seal. Twin CRPS scores the whole sealed distribution; the baselines are point
forecasts, so their CRPS is their absolute error. Lower is better.

| Twin | KPI | Sealed median (80% range) | Actual | Inside 80% | Twin CRPS | Guidance | Same as last quarter | Same quarter last year |
|---|---|---|---|---|---|---|---|---|
| CMG | comparable sales | 2.94 (0.64 to 5.15) | 2.1 | yes | 0.56 | 0.55 | 0.10 | 1.80 |
| CMG | transactions | 1.71 (−0.75 to 4.12) | 0.8 | yes | 0.61 | – | 0.20 | 1.60 |
| CMG | average check | 1.24 (0.05 to 2.41) | 1.3 | yes | 0.22 | – | 0.10 | 0.20 |
| CMG | restaurant-level margin | 25.43 (20.97 to 29.97) | 23.3 | yes | 1.32 | – | 1.90 | 1.20 |
| CMG | revenue growth | 9.53 (−0.01 to 19.15) | 9.6 | yes | – | – | – | – |
| DAL | operating margin (GAAP) | 6.9 (−1.8 to 15.6) | 7.2 | yes | **1.60** | – | 2.23 | 2.90 |
| DAL | revenue growth (GAAP) | 15.2 (10.6 to 19.9) | 21.1 | no | 3.93 | 6.07 | 2.40 | 14.72 |

**Reading it.** Six of seven outcomes landed inside the 80% range, which is what a calibrated 80% interval
should do. The point forecasts are mixed against the simple baselines: Delta's margin beat all of them, and
Chipotle's comparable sales were about as close as guidance but further off than "same as last quarter".

- **Chipotle comparable sales:** the median missed by 0.84 points. The miss came from transactions: the largest
  driver of the sealed forecast was a July–August drop in Chipotle news tone, which hit traffic less than the
  twin expected.
- **Delta revenue:** GAAP revenue includes third-party refinery sales, which rose 76% with fuel prices and added
  about 6.7 points of growth. Delta's guidance excludes them, and on that basis growth was 15.7%, 0.5 points from
  the twin's median. The twin anchored a GAAP KPI on non-GAAP guidance. The lesson is to match each anchor's
  definition to its KPI. The scored result stays GAAP, as sealed.

Sources: Chipotle 8-K accession 0001058090-26-000103, EX-99.1 (2026-10-28); Delta 8-K accession
0000027904-26-000035, EX-99.1 (2026-10-09).

**Pending (sealed in the same files):** Q4 2026 for both twins. Chipotle comparable sales median 4.07
(80% range 1.90 to 6.22); Delta revenue growth median 16.13 (9.44 to 22.97), operating margin 5.95
(−3.28 to 14.93).

## 2. Against the company's own guidance (walk-forward backtest)

| Twin, KPI | Quarters | Twin closer than guidance | CRPS skill vs guidance | Permutation p |
|---|---|---|---|---|
| Delta, revenue growth | 14 | 11 of 14 | +0.29 | 0.005 |
| Chipotle, comparable sales | 18 | 15 of 18 | +0.41 | 0.02 |
| Chipotle, comparable sales vs **analyst consensus** | 6 | 2 of 6 | −0.37 | 0.81 |

Delta beat its own guidance in only 7 of 14 quarters, so its result is not explained by conservative guidance.
Chipotle tends to guide low, so part of its gain may simply correct that bias. Against analyst consensus the
twin shows no edge on the six quarters available.

## 3. Portfolio scorecard

Walk-forward from 2017Q1, refit at every earnings release on data available at that moment. COVID quarters
(2020Q1–2021Q4), and for travel companies the recovery through 2022Q4, are excluded from scoring.
Factory twins use industry defaults with no per-company tuning. CRPS skill = 1 − CRPS(twin) / CRPS(baseline):
positive means the twin is better. Rescored 2026-10-19.

| Ticker | Industry | Built by | Quarters | KPI | MAE twin | MAE last quarter | MAE last year | Skill vs last quarter | Skill vs last year | 80% coverage |
|---|---|---|---|---|---|---|---|---|---|---|
| CMG | restaurant | hand | 30 | transactions | 3.30 | 2.55 | 7.10 | +0.19 | +0.75 | 0.67 |
| CMG | restaurant | hand | 30 | check | 1.23 | 0.77 | 1.07 | -0.10 | +0.46 | 0.69 |
| CMG | restaurant | hand | 30 | comps | 3.13 | 3.69 | 9.21 | +0.21 | +0.67 | 0.80 |
| CMG | restaurant | hand | 30 | rlom | 1.77 | 1.65 | 2.14 | -0.07 | +0.24 | 1.00 |
| CMG | restaurant | hand | 30 | revenue_growth | 3.86 | 3.92 | 9.48 | -0.06 | +0.56 | 0.97 |
| DAL | airline | hand | 27 | revenue_growth | 2.83 | 4.08 | 15.73 | +0.31 | +0.84 | 0.67 |
| DAL | airline | hand | 27 | op_margin | 2.32 | 4.93 | 2.77 | +0.36 | +0.01 | 1.00 |
| AAL | airlines | factory | 26 | revenue_growth | 3.85 | 3.80 | 14.60 | +0.09 | +0.75 | 0.96 |
| AAL | airlines | factory | 26 | op_margin | 2.61 | 5.68 | 4.18 | +0.49 | +0.36 | 0.85 |
| CCL | cruise (hotels template) | factory + LLM | 27 | revenue_growth | 8.51 | 8.68 | 469.78 | +0.02 | +0.98 | 0.67 |
| CCL | cruise (hotels template) | factory + LLM | 27 | op_margin | 9.65 | 10.54 | 11.15 | -0.06 | +0.21 | 0.70 |
| DHI | homebuilders | factory | 30 | revenue_growth | 4.89 | 5.07 | 9.35 | +0.13 | +0.52 | 0.90 |
| DHI | homebuilders | factory | 30 | pretax_margin | 1.20 | 1.36 | 2.22 | +0.10 | +0.46 | 0.97 |
| DRI | restaurants | factory | 31 | revenue_growth | 5.47 | 4.11 | 12.29 | -0.01 | +0.62 | 0.97 |
| DRI | restaurants | factory | 31 | op_margin | 2.18 | 2.02 | 0.92 | +0.10 | +0.02 | 1.00 |
| HLT | hotels | factory | 26 | revenue_growth | 4.73 | 4.55 | 14.30 | -0.05 | +0.67 | 0.88 |
| HLT | hotels | factory | 26 | op_margin | 2.11 | 3.06 | 1.71 | +0.30 | -0.11 | 0.96 |
| LEN | homebuilders | factory | 31 | revenue_growth | 9.52 | 9.27 | 19.69 | -0.06 | +0.52 | 0.81 |
| LEN | homebuilders | factory | 31 | op_margin | 3.38 | 3.75 | 4.17 | +0.18 | +0.18 | 0.69 |
| LUV | airlines | factory | 26 | revenue_growth | 3.19 | 3.37 | 12.82 | +0.07 | +0.78 | 0.85 |
| LUV | airlines | factory | 26 | op_margin | 4.08 | 4.70 | 2.75 | +0.09 | -0.41 | 0.73 |
| MAR | hotels | factory | 26 | revenue_growth | 4.73 | 4.11 | 19.96 | -0.07 | +0.72 | 0.92 |
| MAR | hotels | factory | 26 | op_margin | 2.34 | 2.72 | 1.75 | +0.20 | +0.23 | 0.77 |
| MCD | restaurants | factory | 30 | revenue_growth | 4.08 | 3.80 | 9.80 | -0.02 | +0.58 | 0.90 |
| MCD | restaurants | factory | 30 | op_margin | 3.46 | 3.56 | 4.14 | -0.01 | +0.15 | 0.93 |
| PHM | homebuilders | factory | 27 | revenue_growth | 4.74 | 4.45 | 11.56 | +0.33 | +0.60 | 0.96 |
| PHM | homebuilders | factory | 27 | pretax_margin | 2.32 | 2.46 | 2.59 | +0.68 | +0.55 | 0.96 |
| SBUX | restaurants | factory | 29 | revenue_growth | 6.32 | 5.04 | 10.72 | +0.06 | +0.43 | 0.81 |
| SBUX | restaurants | factory | 29 | op_margin | 2.00 | 2.43 | 3.27 | +0.55 | +0.58 | 0.90 |
| TGT | general_retail | factory | 31 | revenue_growth | 2.84 | 3.08 | 6.11 | +0.02 | +0.47 | 0.74 |
| TGT | general_retail | factory | 31 | op_margin | 1.11 | 1.22 | 1.61 | +0.01 | +0.26 | 0.90 |
| TXRH | restaurants | factory | 29 | revenue_growth | 4.84 | 4.15 | 7.74 | +0.12 | +0.52 | 0.93 |
| TXRH | restaurants | factory | 29 | op_margin | 1.26 | 1.52 | 1.25 | +0.08 | +0.03 | 0.93 |
| UAL | airlines | factory | 26 | revenue_growth | 3.83 | 4.13 | 17.22 | +0.45 | +0.81 | 0.81 |
| UAL | airlines | factory | 26 | op_margin | 2.19 | 4.57 | 2.99 | +0.52 | +0.27 | 1.00 |
| WMT | general_retail | factory | 31 | revenue_growth | 1.23 | 1.21 | 2.62 | -0.00 | +0.50 | 0.87 |
| WMT | general_retail | factory | 31 | op_margin | 0.44 | 0.58 | 0.52 | +0.15 | +0.16 | 0.87 |

The twin beats "same as last quarter" on 26 of 37 KPI series, "same quarter last year" on 35 of 37, and both
on 24 of 37.

**Reading it.** Airlines are strongest, because TSA checkpoint counts and jet fuel prices are timely, direct
sensors. Restaurant and hotel revenue growth roughly ties "same as last quarter": free public data carries little
company-specific information there. The KPI structures of the two hand-built twins were chosen on this same
backtest, so the cleaner tests are the 15 factory twins, which use defaults with no tuning, and the sealed
forecasts above.
