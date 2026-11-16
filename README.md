# Chui Twin

**Turns a public company into a runnable operating model, using only public data.**
3rd place, Longaeva AI Hackathon finals (New York, October 2026).

Public data such as SEC filings, BLS and FRED series, TSA checkpoint counts, news tone, Wikipedia attention
and public store-locator sitemaps is treated as noisy readings of operating states you cannot observe directly:
demand, capacity, price, input cost, labor pressure, sentiment and expansion. One shared engine estimates those
hidden states, runs them forward with Monte Carlo, traces every forecast back to the data behind it, and scores
every company the same way against simple baselines and against management's own guidance.

> This repository is a public showcase: results, method overview and verifiable sealed forecasts.
> The source code is private. Happy to walk through the full system on request.

## How it works

```
public sources ──> adapters ──> point-in-time observations ──┐
  SEC EDGAR / XBRL, FRED, BLS, TSA,     raw response saved     │
  GDELT news tone, Wikimedia, sitemaps  before parsing         v
                                                   engine: estimate hidden states
  industry template: states, causal edges ──────>         -> link states to reported KPIs
  company spec: KPIs, signals, overrides ───────>         -> simulate 10,000 paths
                                                          -> attribute each forecast to its sources
                                                          -> score against baselines
                                                               │
                                     API + dashboard + chat <──┘
```

- **One engine, many companies.** The engine contains no company- or industry-specific code; an automated
  test fails if a ticker or industry term ever appears in it. Industries are described in configuration.
- **17 twins in six industries** (restaurants, retail, airlines, hotels, homebuilders, cruise lines):
  2 built by hand (Chipotle, Delta), 14 built automatically from a ticker with no per-company tuning,
  and Carnival onboarded by an LLM reading its 10-K, an industry no template covered.
- **Every number is traceable** to a filing accession number and exhibit, a URL, or a saved raw snapshot.
- **Point-in-time correct.** Every observation records when it could first have been known, and backtests only
  use data that was public at the forecast time.
- **Legal, public data only.** robots.txt and terms checked for every source; nothing behind a login.

## Results

**Walk-forward backtest** (2017 onward, refit at every earnings release, COVID quarters excluded):

- The twin beats both naive baselines ("same as last quarter" and "same quarter last year") on CRPS in
  **24 of 37** KPI series across the 17 twins.
- **Delta revenue growth vs Delta's own guidance:** the twin was closer in **11 of 14** guided quarters
  (CRPS skill +0.29, exact permutation test p = 0.005).
- **Chipotle comparable sales vs Chipotle's guidance:** CRPS skill **+0.41** over 18 quarters.
- Against analyst consensus (Chipotle comps, 6 quarters available) the twin shows no edge. We do not claim
  an edge over the market.

Details: [docs/results.md](docs/results.md).

## Live test: sealed Q3 2026 forecasts

Each forecast was written to a file, hashed (SHA-256) and timestamped in the Bitcoin blockchain through
OpenTimestamps **before the company reported**, then scored against the earnings release.
**6 of 7 KPIs landed inside the twin's 80% range.**

| Twin | KPI | Sealed | Median (80% range) | Actual | Inside 80% |
|---|---|---|---|---|---|
| CMG | comparable sales, yoy % | Oct 18 | 2.94 (0.64 to 5.15) | 2.1 | yes |
| CMG | transactions, yoy % | Oct 18 | 1.71 (−0.75 to 4.12) | 0.8 | yes |
| CMG | average check, yoy % | Oct 18 | 1.24 (0.05 to 2.41) | 1.3 | yes |
| CMG | restaurant-level margin, % | Oct 18 | 25.43 (20.97 to 29.97) | 23.3 | yes |
| CMG | revenue growth, yoy % | Oct 18 | 9.53 (−0.01 to 19.15) | 9.6 | yes |
| DAL | operating margin, % (GAAP) | Oct 2 | 6.9 (−1.8 to 15.6) | 7.2 | yes |
| DAL | revenue growth, yoy % (GAAP) | Oct 2 | 15.2 (10.6 to 19.9) | 21.1 | no |

- **The miss:** Delta's GAAP revenue includes third-party refinery sales, which rose 76% with fuel prices.
  Delta's guidance excludes them, and on that basis growth was 15.7%, 0.5 points from the twin's median.
  The twin had anchored a GAAP KPI on non-GAAP guidance. The scored result stays GAAP, as sealed.
- **Sources:** Chipotle 8-K accession 0001058090-26-000103 (EX-99.1, filed 2026-10-28); Delta 8-K accession
  0000027904-26-000035 (EX-99.1, filed 2026-10-09).
- **Q4 2026** forecasts for both twins are in the same sealed files and resolve when the companies report
  in early 2027.

### Verify them yourself

The sealed files are in [forecasts/sealed/](forecasts/sealed/), each with its OpenTimestamps proof (`.ots`).

```bash
python verify_seal.py          # recomputes each file's SHA-256 and compares it with the published hash
```

Then drop a `.json` file and its `.ots` proof on https://opentimestamps.org to confirm the Bitcoin timestamp.

| Twin | SHA-256 | Bitcoin block |
|---|---|---|
| DAL | `f6892ab9366122fd81b64c1106b052c1962638c6ab8644587c5baee2d2058bd8` | 969637 (Oct 2026) |
| CMG | `fabe5e811fcf5fe2e0b909a5d7c7e6ff5e69a8ee691645214ec7e816c0016282` | 972040 (Oct 2026) |

## More

- [docs/technical_overview.md](docs/technical_overview.md): method, evaluation protocol, validation and limitations.
- [docs/results.md](docs/results.md): the full portfolio scorecard and the sealed-forecast scoring.

## Copyright

© 2026 Benedict Ngetich. All rights reserved. See [LICENSE](LICENSE). No license is granted to copy,
modify or redistribute any part of this repository.
