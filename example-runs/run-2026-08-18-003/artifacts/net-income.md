# Net Income — run-2026-08-18-003

## Correction Notice (supersedes the previous version of this artifact)

The previous version of this artifact assumed the user's B2B tax form was
**podatek liniowy** (flat 19% linear tax) and, on that assumption, concluded
the stated 25,000 PLN/month must be a **pre-tax/pre-ZUS invoiced (revenue)**
figure, recomputing a lower "true net" of ≈17,773.55 PLN/month.

The user has since corrected two things explicitly:
1. Their actual B2B taxation form is **ryczałt ewidencjonowany** (lump-sum
   tax on revenue), not podatek liniowy.
2. "25,000 PLN is the amount that remains after paying all taxes, including
   ZUS" — i.e. 25,000 PLN/month **is already the fully net, post-tax,
   post-ZUS take-home figure**, not a pre-deduction invoiced amount.

The previous correction does not apply here because it was built entirely on
liniowy's mechanics — in particular its **uncapped 4.9%-of-income health
contribution**, which scales up with revenue and produces a large, growing
deduction at high income levels. Ryczałt's mandatory contributions work
differently (see below) and, as the sanity check in this artifact shows, are
structurally consistent with 25,000 PLN/month being a plausible genuine net
figure at a correspondingly higher (but not implausible) revenue level for a
senior B2B contractor. This artifact now treats **25,000 PLN/month as the
confirmed net income** for downstream use, per the user's explicit
statement, while documenting the ryczałt/ZUS rules that make this plausible
and re-verifying rather than blindly accepting it.

## Gross Income

- Stated by user, now explicitly confirmed as fully **net** (post-tax,
  post-ZUS/health): **25,000 PLN/month** (300,000 PLN/year net).
- The user's actual gross monthly business revenue (before ZUS, health
  contribution, and ryczałt PIT) is **not stated** and is not needed for
  downstream planning now that the net figure is confirmed directly by the
  user. A sanity-check range is derived below purely to check plausibility,
  not to be used as the input figure.

## Jurisdiction & Contract Type

- Country of residence: Poland
- Citizenship: Republic of Poland
- Contract type: B2B / self-employed sole proprietorship (jednoosobowa
  działalność gospodarcza, JDG), invoicing a client — not an employment
  contract.
- Taxation form: **ryczałt ewidencjonowany** (lump-sum tax on revenue), as
  explicitly confirmed by the user. This replaces the podatek liniowy
  assumption used in the previous version of this artifact.
- Tax year modeled: 2026 (rates/thresholds and ZUS/health bases below are
  the 2026 figures current as of the access date; ZUS and health-contribution
  amounts are revised annually and mid-year in Poland).

## Taxes/Contributions

Ryczałt ewidencjonowany taxes revenue directly (no deduction of costs from
the tax base, unlike liniowy/skala), but the mandatory ZUS social
contribution and the health contribution are calculated independently of the
ryczałt tax rate itself, as follows.

1. **Ryczałt PIT rate — depends on business activity classification (PKWiU),
   not on income level**
   - Poland's 2026 ryczałt schedule has multiple statutory rates: 2%, 3%,
     5.5%, 8.5%, 10%, 12%, 12.5%, 14%, 15%, 17%, applied per specific type of
     business activity (services vs. trade vs. professions, etc.) — there is
     no single "the" ryczałt rate; it is determined by what the taxpayer's
     registered activity actually is.
   - For IT/software-service activity specifically, guidance is split: many
     accounting-firm sources treat **12%** as the standard rate for software
     development/programming services, while **8.5%** is argued to apply
     only to narrower IT activities that are not itself "computer programming"
     (e.g. some administration/testing services) — the latter carries
     acknowledged tax-authority scrutiny risk. Higher rates (14%/15%) apply
     to other specific activity types.
   - (source: [mspinfo.pl — Ryczałt w IT i budowlance 2026: stawki i pułapki](https://mspinfo.pl/ryczalt-ewidencjonowany-2026-nowe-stawki-i-wylaczenia-dla-branzy-it-i-budowlanej/), [spksiegowosc.pl — Ryczałt dla programisty w 2026 roku](https://spksiegowosc.pl/blog/ryczalt-dla-programisty-2026-jak-bezpiecznie-stosowac-stawke-85-zamiast-12/), accessed 2026-08-18)
   - **This agent cannot determine the user's exact PKWiU/activity
     classification**, and therefore cannot compute an exact ryczałt PIT
     amount from a gross figure. This is the reason the previous
     reverse-engineering approach (valid under liniowy's single flat 19%
     rate) does not carry over to ryczałt — see Caveats.

2. **ZUS social insurance contributions ("duży ZUS", full rate incl.
   voluntary sickness insurance)**
   - This contribution is a **fixed monthly amount independent of the
     taxation form chosen** (same under ryczałt, liniowy, or skala) —
     confirmed by two independent 2026 sources.
   - Rate/amount for 2026: **1,926.76 PLN/month** (basis: 5,652.60 PLN/month
     = 60% of the projected 2026 average monthly gross wage; includes
     voluntary sickness insurance)
   - (source: [ifirma.pl — Składki ZUS 2026](https://www.ifirma.pl/blog/skladki-zus-2026-ile-wynosza-aktualne-skladki-zus-dla-przedsiebiorcow/), [direct.money.pl — ZUS przedsiębiorcy 2026](https://direct.money.pl/artykuly/porady/zus-przedsiebiorcy-ile-wynosza-skladki-i-jak-je-policzyc), accessed 2026-08-18)

3. **Health insurance contribution (składka zdrowotna) — ryczałt rules
   (materially different from liniowy)**
   - Unlike liniowy (4.9% of income, uncapped, growing with income), under
     ryczałt the health contribution is a **fixed monthly amount determined
     by which of three annual-revenue brackets the taxpayer falls into**,
     based on 9% of a percentage (60%/100%/180%) of the average Q4-2025
     monthly wage (9,228.64 PLN):
     - Annual revenue ≤ 60,000 PLN: **498.35 PLN/month**
     - Annual revenue 60,000.01–300,000 PLN: **830.58 PLN/month**
     - Annual revenue > 300,000 PLN: **1,495.04 PLN/month**
   - Because this is a flat monthly amount within each bracket (not a
     percentage of income), it does **not** scale up materially as revenue
     rises within a bracket — this is the key structural difference from
     liniowy that makes a high, flat net figure like 25,000 PLN/month
     plausible under ryczałt without the large proportional health-deduction
     bite seen under liniowy.
   - 50% of the health contribution paid is deductible from the ryczałt tax
     base (revenue), reducing the PIT amount somewhat but not changing the
     health contribution itself.
   - (source: [pit.pl — Składka zdrowotna 2026 dla ryczałtu ewidencjonowanego](https://www.pit.pl/aktualnosci/skladka-zdrowotna-2026-dla-ryczaltu-ewidencjonowanego-gus-oglosil-wysokosc-podstawy), [gofin.pl — Składka zdrowotna ryczałtowców w 2026 r.](https://www.gofin.pl/skladki-zasilki-emerytury/skladki-zus/45278/skladka-zdrowotna-ryczaltowcow-w-2026-r), accessed 2026-08-18)

Because the exact ryczałt PIT rate depends on a PKWiU classification this
agent does not have, the precise gross-to-net breakdown (amount attributable
to each line item, starting from a gross revenue figure) **cannot be
independently derived** the way it could be reverse-engineered under
liniowy's single flat rate. Given the user's explicit, direct confirmation
that 25,000 PLN/month is already the fully net figure, that confirmed value
is used directly for downstream planning (see Net Income), and the
plausibility of that figure is checked qualitatively below instead.

## Sanity Check (not a re-derivation — a plausibility check only)

Solving for the monthly revenue that would be required to net exactly
25,000 PLN/month after ZUS (1,926.76 PLN), the top health-contribution
bracket (1,495.04 PLN/month, since net income at this level implies annual
revenue is almost certainly above the 300,000 PLN threshold), and the 50%
health-contribution deduction from the ryczałt tax base, at three
representative IT-sector ryczałt rates:

- At 8.5%: required revenue ≈ **30,994 PLN/month** (≈371,925 PLN/year)
- At 12%: required revenue ≈ **32,196 PLN/month** (≈386,347 PLN/year)
- At 15%: required revenue ≈ **33,305 PLN/month** (≈399,666 PLN/year)

(Arithmetic: Revenue × (1 − rate) − ZUS − Health × (1 − 0.5 × rate) =
25,000; solved algebraically per rate above — see Caveats regarding tool
availability for this arithmetic.)

All three scenarios land in the 371,000–400,000 PLN/year revenue range,
i.e. all above the 300,000 PLN/year bracket threshold assumed for the health
contribution, so the bracket assumption used is internally consistent
(no contradiction requiring a different bracket). The implied revenue
(~31,000–33,300 PLN/month) is high but plausible for a senior B2B IT
contractor, and the implied total mandatory-deduction burden is only
roughly 20–22% of revenue — much lower than the ≈28.9% burden computed
under the (incorrect) liniowy assumption in the previous version of this
artifact, because ryczałt's ZUS and health contributions are flat/bracketed
rather than scaling with income the way liniowy's 4.9% health contribution
does. **Conclusion: 25,000 PLN/month as a fully net figure is plausible and
consistent with typical ryczałt outcomes for a high-earning IT B2B
contractor; nothing here is inconsistent enough to flag as implausible.**

## Net Income

- **Confirmed net income (per explicit user statement): 25,000.00 PLN/month**
  (300,000.00 PLN/year), to be used directly and without further deduction
  by `cashflow-analyzer` and downstream planners.
- No further ZUS/health/PIT deduction is applied to this figure — the user
  has stated it is already post-deduction, and the ryczałt sanity check
  above found no structural inconsistency that would contradict this.

## Caveats (flag for `financial-auditor`)

1. **Exact ryczałt rate and exact gross revenue remain unconfirmed and are
   not needed downstream.** The user's exact PKWiU business-activity
   classification (which determines whether their ryczałt rate is 8.5%,
   12%, or another value) was not provided and was not required, since the
   user's net figure is used directly. If a future stage needs the gross
   revenue figure (e.g. for VAT threshold planning or ZUS bracket
   projections), it must be requested from the user rather than inferred
   from this sanity check, which is illustrative only.
2. **`finance-math-toolkit` was not invoked for the sanity-check
   arithmetic.** No Bash/code-execution tool was available in this agent
   session (the tool set provided contained no Bash/shell tool), so the
   algebraic solve in the Sanity Check section above was performed by
   careful manual calculation, not via `scripts/calc.py` (which in any case
   exposes only future-value, required-capital, amortization,
   currency-conversion, and CAGR primitives — no generic tax-solve
   primitive). This is a repeat of the same tool-availability caveat raised
   in the previous version of this artifact. `financial-auditor` should
   independently re-verify the sanity-check arithmetic above per its
   standard recomputation gate, and the coordinator should confirm whether
   a Bash tool is genuinely expected to be available to this agent.
3. **The confirmed net figure is taken from the user's direct statement,
   not independently re-derived line-by-line.** This is appropriate given
   the PKWiU-classification gap above, but is recorded explicitly so
   `financial-auditor` treats it as user-confirmed input rather than an
   independently computed result.
4. VAT is not modeled as a personal income tax (VAT collected on B2B
   invoices is generally a pass-through liability, not personal income,
   assuming the client is a VAT payer and standard VAT settlement applies).
5. The ZUS social contribution figure (1,926.76 PLN/month) assumes "duży
   ZUS" (full-rate, non-preferential) — if the user qualifies for a
   preferential ZUS scheme (e.g. "ulga na start" or "mały ZUS plus"), the
   real contribution would be lower, which is directionally consistent with
   — and does not contradict — the net figure being genuinely achievable at
   a somewhat lower gross revenue than the sanity-check range above.

## Sources

- [mspinfo.pl — Ryczałt w IT i budowlance 2026: stawki i pułapki](https://mspinfo.pl/ryczalt-ewidencjonowany-2026-nowe-stawki-i-wylaczenia-dla-branzy-it-i-budowlanej/) (accessed 2026-08-18)
- [spksiegowosc.pl — Ryczałt dla programisty w 2026 roku - jak bezpiecznie stosować stawkę 8,5% zamiast 12%](https://spksiegowosc.pl/blog/ryczalt-dla-programisty-2026-jak-bezpiecznie-stosowac-stawke-85-zamiast-12/) (accessed 2026-08-18)
- [ifirma.pl — Składki ZUS 2026 - ile wynoszą składki ZUS dla przedsiębiorców?](https://www.ifirma.pl/blog/skladki-zus-2026-ile-wynosza-aktualne-skladki-zus-dla-przedsiebiorcow/) (accessed 2026-08-18)
- [direct.money.pl — ZUS przedsiębiorcy 2026: ile wynoszą składki i jak je policzyć?](https://direct.money.pl/artykuly/porady/zus-przedsiebiorcy-ile-wynosza-skladki-i-jak-je-policzyc) (accessed 2026-08-18)
- [pit.pl — Składka zdrowotna 2026 dla ryczałtu ewidencjonowanego. GUS ogłosił wysokość podstawy](https://www.pit.pl/aktualnosci/skladka-zdrowotna-2026-dla-ryczaltu-ewidencjonowanego-gus-oglosil-wysokosc-podstawy) (accessed 2026-08-18)
- [gofin.pl — Składka zdrowotna ryczałtowców w 2026 r.](https://www.gofin.pl/skladki-zasilki-emerytury/skladki-zus/45278/skladka-zdrowotna-ryczaltowcow-w-2026-r) (accessed 2026-08-18)
- [symfonia.pl — Składka zdrowotna 2026 – ryczałt. Nowe stawki i progi](https://symfonia.pl/blog/rozwoj-firmy/jdg/skladka-zdrowotna-2025-ryczalt/) (accessed 2026-08-18)
- [bizky.ai — Składka zdrowotna ryczałt 2026 – zasady rozliczeń](https://bizky.ai/blog/skladka-zdrowotna-ryczalt-2026-zasady-rozliczen/) (accessed 2026-08-18)
