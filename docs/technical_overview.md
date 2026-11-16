# Chui Twin: Technical Overview

Longaeva AI Hackathon, finals (October 2026). 3rd place.

This overview covers what the system does, how it was tested and where it falls short. It is a shortened
public version of the technical appendix submitted to the judges; implementation details are left out.
Results tables are in [results.md](results.md).

## 1. What the system does

Chui Twin turns a public company into a runnable operating model. Public data is treated as **noisy sensors of
hidden operating states**: demand, capacity, price, input cost, labor, sentiment and expansion. One shared engine:

1. estimates those states each quarter,
2. links them to the KPIs the company reports through a causal graph,
3. simulates the next quarters with Monte Carlo,
4. traces every forecast back to the data behind it,
5. scores every twin the same way against simple and expert baselines.

The claim is about **the system, not one company**. Seventeen twins in six industries run on the same engine.
Fifteen of them were built automatically from the ticker alone with no per-company tuning; one of those
(Carnival, an industry no template covered) was onboarded with an LLM reading the 10-K.

## 2. Where an edge would come from

Prices move on the gap between reported results and what the market expected. An information edge, here, means
knowing before the release, from data that was public at the time, where the reported KPIs will land relative to
that expectation.

The twin models the company's operations: a few hidden states drive the reported KPIs, those states move weeks
before they are reported, and public data watches them move (TSA checkpoint counts and jet fuel prices for an
airline; restaurant sales, wages, store counts and news tone for a restaurant chain).

From data to an edge is a chain of three links, and each needs its own evidence:

| Link | Evidence so far |
|---|---|
| 1. Public sensors track the hidden states | The twin beats both naive baselines on 24 of 37 KPI series |
| 2. The twin knows more than the expectation | Beats management guidance on accuracy (Delta revenue: closer in 11 of 14 quarters, p = 0.005; Chipotle comps: skill +0.41 over 18 quarters). Loses to analyst consensus on the 6 Chipotle quarters available |
| 3. That knowledge is not already in the price | Not tested |

We do not claim a demonstrated edge over the market. What is built is the system that would generate one and
the instrument that measures honestly whether it does. Testing it needs point-in-time consensus history for
every twin and an earnings-day event study, and the sealed live forecasts keep adding a record that cannot be
fitted after the fact.

## 3. Architecture

| Layer | Role | What a new company or industry needs |
|---|---|---|
| Engine | estimation, calibration, simulation, attribution, evaluation, sealing | nothing: an automated test fails if any ticker, state name or series name appears in it |
| Data adapters | SEC EDGAR and XBRL, FRED, BLS, TSA, Wikimedia, GDELT, a public-sitemap counter with Internet Archive history | usually nothing |
| Industry templates | an industry's states, default causal edges with priors, KPI structure | one configuration file per industry |
| Onboarding | ticker → SEC industry code → template → company spec; optionally an LLM reads the 10-K and proposes additions | the ticker |
| Company specs | KPIs, signals, overrides | written by hand (2) or generated (15) |

A second test runs the full engine end to end on a dummy industry with made-up state names, which proves that
adding an industry is configuration, not code.

## 4. Data and point-in-time correctness

- **Coverage:** 55 signal series (about 139,000 observations) from 6 public sources, plus 2,190 reported KPI
  values from SEC filings for 17 companies, 56 management-guidance values and 6 consensus values.
- **Raw first:** every fetch is saved untouched before parsing, so a parser can be fixed and rerun.
- **Point in time:** every observation stores the period it describes and when it could first have been known.
  Release lags are set conservatively, reported results are dated at the earnings press release, and daily
  signals become available the day after the day they describe. A backtest at time *t* uses only data available
  at *t*.
- **Traceability:** every value carries its source: URL, SEC accession number and exhibit, raw snapshot path,
  and for text extractions the exact sentence it came from.
- **Legal data only:** robots.txt and terms checked for every source; nothing requires a login. Chipotle menu
  prices were not scraped, because they sit behind an API key in the site's JavaScript.
- **Known caveat:** FRED and BLS serve the latest data vintage, so revised macro values can leak a little
  hindsight into old backtest quarters. Market prices and counts are not revised.

## 5. Model

Kept deliberately simple: about 30 scored quarters per twin cannot support a complex model.

1. **Signals → states:** each signal is a noisy reading of one hidden state, weighted by its reliability and
   by how fresh it is. Each signal's share of each state is stored, so every forecast decomposes into sources.
2. **States → KPIs:** Bayesian linear regression with priors from the causal graph. A KPI can be modeled as a
   level, a change since the last report, or a surprise relative to the latest published guidance or consensus.
3. **Identities and bounds:** accounting identities such as comps = transactions + average check hold on every
   simulated path, and physical bounds are enforced.
4. **Simulation:** fully vectorized Monte Carlo. A 10,000-path forecast takes about 0.03 s on a laptop.
5. **Attribution:** a driver waterfall, each bar linked to its sources, plus leave-one-signal-out
   counterfactuals.
6. **Scenarios:** shocks propagate through the causal graph and decay over time. Decay rates for the preset
   shocks were measured from real events: Chipotle's 2015 food-safety crisis decayed with a half-life of about
   7.4 quarters, and COVID's hit to airlines and hotels with about 3.9.

## 6. Evaluation protocol

- **Walk-forward:** for each reported quarter, the forecast is made one hour before the earnings release, and
  everything is refit from scratch on data available at that moment. Tested from 2017Q1.
- **Excluded from scoring:** the COVID quarters (2020Q1–2021Q4), and the travel recovery through 2022Q4.
- **Baselines:** same as last quarter, same quarter last year, management guidance, and analyst consensus where
  public. The headline counts series that beat **both** naive baselines, since which one is harder depends on
  the KPI.
- **Metrics:** MAE, CRPS (scores the whole forecast distribution, not just the point) and 80% interval coverage.
  Skill = 1 − CRPS(twin) / CRPS(baseline) on the same quarters.
- **Sealed live forecasts:** each forecast is written to a file, hashed, and timestamped in Bitcoin through
  OpenTimestamps before the company reports. Outcomes are accepted only if they became public after the seal.
  The files and proofs are in this repository.

## 7. Validating extracted data

Automatic checks run on every one of the 2,190 reported values: the source sentence appears verbatim in the
saved filing and its number equals the stored value (154 of 154 text extractions pass); accounting identities
hold on reported values (14 of 14); values sit inside physical limits; and outliers beyond 4 sd are flagged for
review (23 flagged, all real events such as COVID and large one-off write-downs). People then review a
fixed-seed random sample plus everything flagged.

## 8. LLM onboarding: the model proposes, code decides

For a company no template covers, an LLM reads the latest 10-K alongside a menu of what the system can actually
use, and proposes a template, extra driver series and extra KPIs. Every proposal must quote the 10-K. Code, not
the model, then accepts or rejects each one against the filing and the available data, and records the reason.

Carnival was the first twin built this way. Rerunning four existing twins with the LLM step changed their
accuracy by at most ±0.06 in skill, inside the noise. Its value is coverage rather than accuracy: it onboards
new industries and finds company-specific KPIs that forecast better than naive. New KPIs it proposes are checked
by a person before they are scored.

## 9. Scope and roadmap

The system models companies whose results come from observable operating drivers: restaurants, retail,
airlines, hotels, homebuilders and cruise lines today. Banks need a new template (deposits, credit quality,
margin), and binary-event companies such as clinical-stage biotech need a separate event module; both fit
the existing engine. Next steps: point-in-time consensus history and an earnings-day event study to test for
a market edge, earnings-call guidance, and industries that reuse existing data sources (trucking, rail).

## 10. Limitations

- **Short histories:** about 26–31 scored quarters per KPI. Skill differences under about 0.05 are noise.
- **A forecasting model, not a structural one:** scenario moves far outside history are extrapolation, and the
  dashboard says so.
- **Causal edges** come from priors, and are validated rather than discovered.
- **Selection bias:** the two hand-built twins' KPI structures were chosen on the reported backtest.
- **Guidance from press releases only:** guidance given only on earnings calls is missed.
- **No call transcripts, reviews or forums:** their sources are licensed or restrict this use.
- **LLM hindsight:** the LLM reads today's 10-K, and the backtest scores the resulting structure on earlier
  quarters. Its instructions forbid using known outcomes, but that cannot be verified.

---

© 2026 Benedict Ngetich. All rights reserved.
