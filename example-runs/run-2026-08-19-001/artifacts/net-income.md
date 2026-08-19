# Net Income — Poland, B2B Self-Employed IT Contractor

## Gross Income

- **12,000.00 PLN/month** gross, before any deductions (per `requirements.md`).
- Annualized for bracket-lookup purposes: 12,000 × 12 = **144,000 PLN/year**.

## Jurisdiction & Contract Type

- Country of residence / tax residence: **Poland**.
- Citizenship: **Polish** (no cross-border tax treaty considerations apply).
- Contract type: **B2B, self-employed sole proprietorship (jednoosobowa działalność
  gospodarcza / JDG)**, freelance IT contractor, no employer — i.e. the
  contractor is both the "payer" and the "insured", responsible for
  remitting their own ZUS contributions and income tax (no withholding by a
  client).

### Assumptions made (not stated in requirements — flagged as caveats below)

1. **Tax form: ryczałt ewidencjonowany (flat-rate tax on revenue) at 12%.**
   This is the standard statutory rate for IT/software-related services
   (PKWiU categories covering software development, systems/network
   management) under the current classification, and is a common choice for
   solo IT contractors with low deductible costs. `requirements.md` does not
   state which of the three available PIT regimes (ryczałt / podatek liniowy
   19% / skala podatkowa 12%–32%) the contractor has actually elected — **this
   is a genuine open item, not a jurisdiction ambiguity**, since the choice is
   the taxpayer's own election, not fixed by law. If the contractor has
   actually elected podatek liniowy or skala podatkowa, net income would
   differ materially (see Caveats).
2. **ZUS regime: standard full-rate social security ("duży ZUS"), with the
   voluntary sickness contribution included.** The contractor's annual
   revenue (144,000 PLN) exceeds the 120,000 PLN previous-year revenue cap
   for "Mały ZUS Plus" relief, so that relief is **not** available regardless
   of how long the business has been running — this part is confirmed, not
   an assumption. However, `requirements.md` does not state how long the
   contractor has been operating the business; if this is within the first
   6 months ("Ulga na start" — exemption from social contributions, health
   contribution only) or within the first 24 months on preferential ZUS
   (reduced-basis social contributions), the ZUS figure below would be
   substantially lower. **Flagged as a caveat** — assumed here to be an
   established/ongoing business past any start-up relief period, consistent
   with "current gross income" describing a steady state.

## Taxes/Contributions

All figures are monthly, in PLN, for 2026.

### 1. ZUS social security contributions ("duży ZUS", standard rate)

| Component | Rate | Amount (PLN) |
|---|---|---|
| Emerytalna (pension) | 19.52% of 5,652.60 PLN basis | 1,103.27 |
| Rentowa (disability) | 8.00% of basis | 452.16 |
| Chorobowa (sickness, voluntary) | 2.45% of basis | 138.47 |
| Wypadkowa (accident, ≤9 insured) | 1.67% of basis | 94.39 |
| Fundusz Pracy (Labor Fund) | 2.45% of basis | 138.47 |
| **Total ZUS social contributions** | | **1,926.76** |

(source: [Co w zus 2026 — proplanum.com](https://www.proplanum.com/blog/zus-2026), accessed 2026-08-19; cross-checked against [Składki ZUS w 2026 r. dla przedsiębiorców — symfonia.pl](https://symfonia.pl/blog/firmy/male-firmy/skladki-zus-w-2026-r-dla-przedsiebiorcow-ile-wyniosa/), accessed 2026-08-19)

Confirmation that standard "duży ZUS" applies (not "Mały ZUS Plus"): the
120,000 PLN/year previous-year revenue cap for Mały ZUS Plus is exceeded by
this contractor's 144,000 PLN annualized revenue (source: [Mały ZUS Plus 2026
– 36 miesięcy ulgi i limit 120 tys. zł — bizky.ai](https://bizky.ai/blog/maly-zus-plus-2025/),
accessed 2026-08-19).

### 2. Health insurance contribution (składka zdrowotna) — ryczałt payer

Ryczałt payers pay a fixed monthly health contribution set by cumulative
annual revenue bracket (not by profit):

| Annual revenue bracket | Monthly contribution |
|---|---|
| up to 60,000 PLN | 498.35 PLN |
| 60,000–300,000 PLN | 830.58 PLN |
| over 300,000 PLN | 1,495.04 PLN |

At 144,000 PLN/year the contractor falls in the middle bracket:
**830.58 PLN/month.**

(source: [Składka zdrowotna 2026 – ryczałt. Nowe stawki i progi — symfonia.pl](https://symfonia.pl/blog/rozwoj-firmy/jdg/skladka-zdrowotna-2025-ryczalt/), accessed 2026-08-19; corroborated by [Składka zdrowotna dla ryczałtu w 2026 r. — infakt.pl](https://www.infakt.pl/blog/skladka-zdrowotna-dla-ryczaltu-w-2026-r/), accessed 2026-08-19)

### 3. Income tax — ryczałt ewidencjonowany, 12%

Ryczałt tax base = gross revenue − ZUS social contributions paid (fully
deductible) − 50% of the health contribution paid (partially deductible
from the ryczałt base; the other 50% is not deductible from either the base
or the tax) (source: [Kalkulator ryczałtu 2026 — calkulator.pl](https://calkulator.pl/podatki/kalkulator-ryczaltu/), accessed 2026-08-19; [Ryczałt 2026 – komu się opłaca i jak rozliczać — amavat.pl](https://amavat.pl/ryczalt-co-musze-wiedziec/), accessed 2026-08-19).

- Taxable base = 12,000.00 − 1,926.76 − (830.58 × 50%)
  = 12,000.00 − 1,926.76 − 415.29 = **9,657.95 PLN**
- Rate for IT/software-related services: **12%** (source: [Ryczałt w IT: stawki, zasady i zastosowanie w 2026 roku — kurdynowski.com.pl](https://kurdynowski.com.pl/ryczalt-w-it-stawki-zasady-i-zastosowanie-w-2026-roku/), accessed 2026-08-19; [Ryczałt dla programisty – 8,5% czy 12%? — ifirma.pl](https://www.ifirma.pl/blog/jaki-ryczalt-dla-programisty-85-czy-12-stawka-ryczaltu-dla-informatykow/), accessed 2026-08-19)
- Tax = 12% × 9,657.95 = **1,158.95 PLN**

### 4. VAT (informational — not a deduction from net income)

As a B2B service provider the contractor is very likely VAT-registered (or
could opt for the ≤200,000 PLN/year "zwolnienie podmiotowe" exemption, since
144,000 PLN/year is under that cap — the contractor's actual VAT status is
not stated in `requirements.md`). For domestic B2B invoicing, VAT is charged
on top of the net invoice amount and passed through to the tax office — it
is **not** a deduction from the contractor's own income, so it is excluded
from the net income calculation below. Flagged as a caveat only in case the
contractor's actual client base is such that VAT registration creates cash
administrative burden, not a net income effect. (source: [Ryczałt dla
programisty – jakie podatki, składki i zasady — podatkiprogramisty.pl](https://podatkiprogramisty.pl/ryczalt-programisty-jakie-podatki-placi-programista-na-ryczalcie/), accessed 2026-08-19)

## Net Income

| Line | Amount (PLN) |
|---|---|
| Gross income | 12,000.00 |
| − ZUS social contributions | −1,926.76 |
| − Health insurance contribution | −830.58 |
| − Income tax (ryczałt 12%) | −1,158.95 |
| **= Net monthly income** | **8,083.71** |

**Net monthly income ≈ 8,083.71 PLN** (≈ 67.4% of gross), under the stated
assumptions (ryczałt 12%, standard full ZUS, established ongoing business).

## Caveats for `financial-auditor`

1. **Tax regime not confirmed by the user.** This computation assumes ryczałt
   ewidencjonowany at 12%, the common/statutory rate for IT services. If the
   contractor has actually elected podatek liniowy (19% flat tax on
   profit, deductible costs, different health-contribution rule — 4.9% of
   income with a 2026 minimum of 432.54 PLN/month) or skala podatkowa
   (progressive 12%/32%), net income would differ and this artifact should
   be regenerated with the correct regime once confirmed.
2. **Business tenure / ZUS relief eligibility not confirmed by the user.**
   Standard full-rate "duży ZUS" is used here. Mały ZUS Plus is confirmed
   inapplicable (revenue exceeds its 120,000 PLN/year cap), but "Ulga na
   start" (first 6 months) or preferential 24-month reduced-basis ZUS were
   not ruled out by `requirements.md`. If either applies, ZUS contributions
   — and therefore net income — would be higher than shown here.
3. **VAT registration status not stated.** Treated as net-income-neutral
   (pass-through), which holds under normal domestic B2B invoicing
   regardless of registration status, but flagged in case the contractor's
   client mix involves reverse-charge/export scenarios not covered by
   `requirements.md`.

## Sources

- [Co w zus 2026: duży ZUS 1926,76 zł, zdrowotna 432,54 zł — proplanum.com](https://www.proplanum.com/blog/zus-2026) (accessed 2026-08-19)
- [Składki ZUS w 2026 r. dla przedsiębiorców – ile wynoszą? — symfonia.pl](https://symfonia.pl/blog/firmy/male-firmy/skladki-zus-w-2026-r-dla-przedsiebiorcow-ile-wyniosa/) (accessed 2026-08-19)
- [Składka zdrowotna 2026 – ryczałt. Nowe stawki i progi — symfonia.pl](https://symfonia.pl/blog/rozwoj-firmy/jdg/skladka-zdrowotna-2025-ryczalt/) (accessed 2026-08-19)
- [Składka zdrowotna dla ryczałtu w 2026 r. — infakt.pl](https://www.infakt.pl/blog/skladka-zdrowotna-dla-ryczaltu-w-2026-r/) (accessed 2026-08-19)
- [Składka zdrowotna 2026 – skala podatkowa, podatek liniowy, ryczałt i inne formy — infakt.pl](https://www.infakt.pl/blog/skladka-zdrowotna-2026-skala-podatkowa-podatek-liniowy-ryczalt-i-inne-formy/) (accessed 2026-08-19)
- [Ryczałt w IT: stawki, zasady i zastosowanie w 2026 roku — kurdynowski.com.pl](https://kurdynowski.com.pl/ryczalt-w-it-stawki-zasady-i-zastosowanie-w-2026-roku/) (accessed 2026-08-19)
- [Ryczałt dla programisty – 8,5% czy 12%? Stawka ryczałtu w IT — ifirma.pl](https://www.ifirma.pl/blog/jaki-ryczalt-dla-programisty-85-czy-12-stawka-ryczaltu-dla-informatykow/) (accessed 2026-08-19)
- [Kalkulator ryczałtu 2026 — calkulator.pl](https://calkulator.pl/podatki/kalkulator-ryczaltu/) (accessed 2026-08-19)
- [Ryczałt 2026 – komu się opłaca i jak rozliczać — amavat.pl](https://amavat.pl/ryczalt-co-musze-wiedziec/) (accessed 2026-08-19)
- [Ryczałt dla programisty – jakie podatki, składki i zasady — podatkiprogramisty.pl](https://podatkiprogramisty.pl/ryczalt-programisty-jakie-podatki-placi-programista-na-ryczalcie/) (accessed 2026-08-19)
- [Mały ZUS Plus 2026 – 36 miesięcy ulgi i limit 120 tys. zł — bizky.ai](https://bizky.ai/blog/maly-zus-plus-2025/) (accessed 2026-08-19)
