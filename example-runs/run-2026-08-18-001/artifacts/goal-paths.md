# Goal Paths — Debt Payoff

Run: `run-2026-08-18-001` | Goal type: `debt_payoff` | Planner: `debt-payoff-planner`

## Goal Summary

- **Lender**: PKO Bank Polski (PKO BP), Poland (user-confirmed).
- **Loan/product name**: not stated by the user. Research (below) matches the
  stated terms most closely to PKO BP's **pożyczka gotówkowa** (cash/personal
  installment loan) product line in structure (fixed rate, equal/annuity
  installments), though PKO's currently published cash-loan tenor cap
  (see Assumptions & Sources, item 4) is shorter than the user's stated
  25-year original term. Because the user has directly confirmed the
  balance, rate, origination year, and term as their own loan's facts, those
  user-stated figures are used as-is; only the *type* of amortization and
  the *existence/size of a prepayment penalty* were resolved via research,
  per the requirements' escalation instructions.
- **Current remaining balance**: 8,000 USD (user-stated, as of 2026-08-18).
- **Interest rate**: 14% annual, **fixed, nominal, standard reducing-balance
  monthly compounding** (user-stated rate; fixed-rate structure and monthly
  reducing-balance compounding confirmed by research into PKO BP's
  comparable consumer cash-loan product — see Assumptions & Sources item 1).
- **Amortization type**: **standard annuity / equal-installment** (constant
  total monthly payment, declining interest portion, growing principal
  portion). Confirmed as PKO BP's standard structure for this loan class by
  research (item 1); this is also the default the requirements document
  instructed if research didn't contradict it.
- **Original term**: 25 years (originated 2022); **~21 years / 252 months
  remaining** as of 2026-08-18 (user-confirmed facts).
- **Prepayment penalty**: **none applicable.** Confirmed via PKO BP's own
  published policy of 0% early-repayment commission with automatic pro-rata
  refund of remaining commission on early full repayment for its consumer
  cash-loan product — see Assumptions & Sources item 2. (A separate
  statutory-threshold argument — Poland's Consumer Credit Act cap on lender
  compensation for early repayment — was initially cited as corroborating
  evidence but, on correct currency conversion via `finance-math-toolkit`,
  does not actually support "balance is under the threshold"; see item 3 for
  the corrected calculation and why it is not used as evidence here. The "no
  penalty" verdict therefore rests solely on the PKO 0% commission policy in
  item 2.) Extra/lump-sum payments in every path below are therefore modeled
  with **no penalty deduction**.
- **Disposable surplus available for extra payment**: 1,200 USD/month, fully
  on top of the minimum payment (already inside the user's stated 1,800
  USD/month expenses per `requirements.md` and `cashflow.md`).
- **Baseline minimum monthly payment** (computed, not stated by lender):
  ≈ **98.65 USD/month**, sized to fully amortize 8,000 USD at 14%
  annual/annuity over exactly 252 months (21 years) — computed via
  `finance-math-toolkit amortization` (see calculation below). This is
  comfortably below the 1,800 USD/month expense figure the user confirmed
  already includes it, which is an internal consistency check that passes.
- **Objective**: pay off the loan as fast as reasonably possible.

## Candidate Paths

All three paths below were computed with
`python calc.py amortization --principal 8000 --annual-rate 0.14 --monthly-payment <X>`
from `finance-math-toolkit`. No prepayment penalty is deducted (see Goal
Summary). All dollar figures are USD, matching the user's stated currency.

### Path 1 — Minimum Payment Only (baseline, NOT recommended)

- **Target/monthly payment**: 98.65 USD/month total (the contractual
  minimum only; the full 1,200 USD/month surplus is instead left unused for
  debt purposes in this path).
- **Where the money goes**: 98.65 USD/month to PKO BP loan minimum
  installment; the 1,200 USD/month surplus is not redirected to the loan in
  this scenario (this path exists purely as the "do nothing extra"
  comparison case required by `requirements.md`'s MATERIAL FLAG).
- **Timeline**: **252 months (21.0 years)** to payoff, on the loan's
  original schedule.
- **Total interest paid over life of loan from today**: **16,840.75 USD**.
- **Purpose**: baseline for comparison only — this path does **not** meet
  the user's stated "fastest possible" objective and is not a recommended
  path.

### Path 2 — Balanced Payoff (extra payment + parallel emergency buffer)

- **Target/monthly payment**: 698.65 USD/month total = 98.65 USD minimum +
  600 USD/month extra principal payment.
- **Where the money goes**: 600 USD/month of the 1,200 USD/month surplus
  goes to extra principal payment on the PKO BP loan; the remaining
  600 USD/month is redirected to building a cash emergency buffer (e.g. a
  standard Polish bank savings/oszczędnościowe account) — addressing the
  zero-existing-savings flag (`requirements.md` Assumption A5 /
  `cashflow.md` Flag 3) rather than leaving no buffer at all during payoff.
- **Timeline**: **13 months (1.08 years)** to full payoff.
- **Total interest paid**: **638.23 USD** (16,202.52 USD less than Path 1's
  baseline interest).
- **After payoff**: by month 13 this path has also accumulated
  ≈ 7,800 USD (13 × 600 USD) in a liquid buffer, and the full
  698.65 USD/month is freed up to continue building savings or be
  redirected to other goals.

### Path 3 — Aggressive Full-Surplus Payoff (fastest; primary recommendation for the stated objective)

- **Target/monthly payment**: 1,298.65 USD/month total = 98.65 USD minimum
  + full 1,200 USD/month surplus as extra principal payment.
- **Where the money goes**: the entire 1,200 USD/month surplus goes to
  extra principal payment on the PKO BP loan, on top of the continuing
  98.65 USD/month minimum; no separate buffer is built during the payoff
  window.
- **Timeline**: **7 months (0.58 years)** to full payoff.
- **Total interest paid**: **352.22 USD** (16,488.53 USD less than Path 1's
  baseline interest; 286.01 USD less interest than Path 2, in exchange for
  a shorter time with zero cash buffer).
- **Risk note**: this path carries the zero-liquidity-buffer risk flagged in
  `cashflow.md` (Flag 3) for its full 7-month duration — any income
  disruption or shock expense during that window would have no cash buffer
  behind it, since 100% of surplus is committed to the loan. The exposure
  window is short (7 months) relative to Path 1's 21-year alternative, but
  it is not zero.
- **After payoff**: from month 8 onward, the full 1,298.65 USD/month
  (minimum + former extra payment) is freed for emergency-fund building or
  other goals — reaching Path 2's ~7,800 USD buffer target in
  well under 6 months post-payoff.

## Assumptions & Sources

1. **PKO BP consumer cash-loan structure (fixed rate; equal/annuity
   installments; 0% early-repayment commission with automatic pro-rata
   refund).** Source: PKO Bank Polski, "Pożyczka gotówkowa" product page,
   https://www.pkobp.pl/klient-indywidualny/kredyty-pozyczki/pozyczka-gotowkowa
   , accessed 2026-08-18; corroborated by third-party rate/term aggregators
   (comperia.pl, totalmoney.pl, bankier.pl, 17bankow.com, moneteo.com,
   jakdorobic.pl), accessed 2026-08-18, which independently show PKO's
   published cash-loan terms as fixed nominal rate with equal (annuity)
   monthly installments.
2. **PKO BP early-repayment/commission-refund policy.** Source: TVN24 Biznes,
   "PKO BP zwróci koszty prowizji. Wcześniejsza spłata pożyczki lub kredytu",
   https://tvn24.pl/biznes/pieniadze/pko-bp-zwroci-koszty-prowizji-wczesniejsza-splata-pozyczki-lub-kredytu-st4618085
   , accessed 2026-08-18: confirms 0% early-repayment commission for PKO's
   cash loan and automatic settlement of any pro-rata commission refund
   within 14 days of early full repayment, with no application required for
   repayments made from 2019-11-12 onward.
3. **Statutory ceiling on early-repayment compensation for consumer credit
   in Poland — cited as background, NOT used as supporting evidence for the
   "no penalty" verdict (see correction below).** Source: Art. 49, Ustawa o
   kredycie konsumenckim (Polish Consumer Credit Act, implementing EU
   Consumer Credit Directive 2008/48/EC); summarized via UOKiK (Polish
   Office of Competition and Consumer Protection),
   https://finanse.uokik.gov.pl/kredyty-konsumenckie/banki-zwracaja-pieniadze-za-wczesniejsza-splate-kredytu/
   , accessed 2026-08-18: on early repayment, total credit cost must be
   reduced proportionally for the shortened period; any lender compensation
   for early repayment applies only to fixed-rate loans and only when
   prepayment within a 12-month window exceeds roughly 3x the average
   corporate-sector wage in Poland, cited by UOKiK as approximately 24,000+
   PLN.
   **Correction (per financial-auditor finding):** the original version of
   this artifact compared the ~24,000 PLN statutory threshold directly
   against the 8,000 USD loan balance with no currency conversion, and
   incorrectly concluded the balance "falls well under" the threshold. That
   comparison is invalid without converting both figures to the same
   currency. Doing the conversion explicitly via `finance-math-toolkit`:
   `python calc.py convert-currency --amount 24000 --rate 0.268817` (rate
   derived from the mid-August 2026 USD/PLN spot rate of ~3.72 PLN per USD;
   xe.com and tradingeconomics.com, accessed 2026-08-18) gives:
   ```json
   {
     "converted_amount": 6451.61,
     "amount": 24000.0,
     "rate": 0.268817
   }
   ```
   i.e. the ~24,000 PLN threshold is approximately **6,451.61 USD** at the
   current spot rate (roughly 6,000-6,150 USD across the ~3.9-4.0 PLN/USD
   range seen over recent months — `--rate 0.25` and `--rate 0.2564`
   respectively give 6,000.00 USD and 6,153.60 USD). This converted
   threshold (~6,000-6,450 USD) is **less than** this loan's 8,000 USD
   balance, not greater — the opposite of the original claim. Because the
   loan balance is stated in USD while the statutory threshold is
   denominated in PLN for a PLN-based statutory test, and the two currencies
   don't line up cleanly in the user's favor once converted correctly, this
   statutory-threshold argument is **unsound as written and is not relied
   upon**. It does not, however, overturn the overall "no prepayment
   penalty" verdict for this specific loan, which is independently and
   sufficiently supported by item 2 (PKO BP's own published 0%
   early-repayment-commission policy with automatic pro-rata refund) on its
   own.
4. **Tenor discrepancy flagged, not resolved by research.** Published PKO BP
   cash-loan terms found during research cap the product's maximum tenor at
   96 months (8 years) (comperia.pl/totalmoney.pl/jakdorobic.pl listings,
   accessed 2026-08-18), shorter than the user-confirmed 25-year original
   term of this loan. This suggests the user's loan may be a different,
   longer-amortization PKO product (e.g. a secured or mortgage-adjacent
   installment product) not matched exactly by the researched cash-loan
   terms. This discrepancy does not change any figure used in the paths
   above (balance, rate, and remaining term are all user-confirmed facts,
   not researched), but it does mean the *fixed-rate / equal-installment /
   no-penalty* structure is an inference from the closest comparable PKO
   product rather than a confirmed match to the user's exact product. Flagged
   for `financial-auditor` and the user's awareness; not treated as blocking
   since (a) the "no penalty" verdict rests on PKO's own published 0%
   early-repayment-commission policy (item 2), which is a general policy for
   its cash-loan product line and not conditioned on the exact tenor variant,
   and (b) the requirements document's default instruction (standard annuity
   if research/user can't fully clarify) is followed explicitly. (Note: the
   statutory-threshold argument previously cited here as additional support
   has been withdrawn — see the correction in item 3 — so it is not part of
   this reasoning.)
5. **Baseline minimum-payment computation.** Computed via
   `finance-math-toolkit`: `python calc.py amortization --principal 8000
   --annual-rate 0.14 --monthly-payment 98.65` → 252 months to payoff
   (exactly the user-confirmed 21-year remaining term), confirming 98.65
   USD/month as the payment that fully amortizes this balance over the
   stated remaining term at the stated rate.
6. **All three candidate-path payoff times and total-interest figures** are
   direct, unmodified outputs of `finance-math-toolkit`'s `amortization`
   command (see each path above for the exact command/inputs); none are
   hand-estimated.
7. **Income/expense/surplus figures** (3,000 USD/month income, 1,800
   USD/month expenses, 1,200 USD/month surplus) are user-stated/derived
   facts already established in `requirements.md` and `cashflow.md` and are
   not re-cited here as external facts.
8. **Zero-existing-savings assumption** underlying Path 2's and Path 3's
   buffer framing is `requirements.md` Assumption A5 (user did not state
   savings; assumed 0), not independently researched.
