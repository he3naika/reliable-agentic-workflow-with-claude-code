#!/usr/bin/env python3
"""Deterministic financial calculations for the Personal Finance Goal Planner.

Every subcommand prints a single JSON object to stdout. This exists so that
agents never estimate compound growth, safe-withdrawal capital, amortization,
or currency conversion in prose — they call this script and use the exact
result.

Usage:
    python calc.py future-value --principal 0 --contribution 400 --annual-rate 0.072 --years 13
    python calc.py required-capital --target-monthly-income 2000 --swr 0.04
    python calc.py amortization --principal 8000 --annual-rate 0.14 --monthly-payment 1200
    python calc.py convert-currency --amount 1000 --rate 0.23
"""
import argparse
import json
import sys


def future_value(principal: float, contribution: float, annual_rate: float, years: float) -> dict:
    months = round(years * 12)
    monthly_rate = annual_rate / 12
    if monthly_rate == 0:
        fv = principal + contribution * months
    else:
        growth = (1 + monthly_rate) ** months
        fv = principal * growth + contribution * ((growth - 1) / monthly_rate)
    return {
        "future_value": round(fv, 2),
        "principal": principal,
        "monthly_contribution": contribution,
        "annual_rate": annual_rate,
        "years": years,
        "months": months,
    }


def required_capital(target_monthly_income: float, swr: float) -> dict:
    if swr <= 0:
        raise ValueError("safe withdrawal rate must be > 0")
    annual_income = target_monthly_income * 12
    capital = annual_income / swr
    return {
        "required_capital": round(capital, 2),
        "target_monthly_income": target_monthly_income,
        "target_annual_income": annual_income,
        "safe_withdrawal_rate": swr,
    }


def amortization(principal: float, annual_rate: float, monthly_payment: float, max_months: int = 1200) -> dict:
    monthly_rate = annual_rate / 12
    balance = principal
    total_interest = 0.0
    months = 0

    if monthly_rate > 0 and monthly_payment <= balance * monthly_rate:
        return {
            "error": "monthly_payment does not cover the first month's interest — balance would never decrease",
            "principal": principal,
            "annual_rate": annual_rate,
            "monthly_payment": monthly_payment,
            "first_month_interest": round(balance * monthly_rate, 2),
        }

    while balance > 0 and months < max_months:
        interest = balance * monthly_rate
        principal_payment = min(monthly_payment - interest, balance)
        balance -= principal_payment
        total_interest += interest
        months += 1

    return {
        "months_to_payoff": months,
        "years_to_payoff": round(months / 12, 2),
        "total_interest_paid": round(total_interest, 2),
        "principal": principal,
        "annual_rate": annual_rate,
        "monthly_payment": monthly_payment,
        "reached_max_months": months >= max_months,
    }


def convert_currency(amount: float, rate: float) -> dict:
    return {
        "converted_amount": round(amount * rate, 2),
        "amount": amount,
        "rate": rate,
    }


def cagr(start_price: float, end_price: float, years: float) -> dict:
    if start_price <= 0 or years <= 0:
        raise ValueError("start_price and years must be > 0")
    rate = (end_price / start_price) ** (1 / years) - 1
    return {
        "cagr": round(rate, 4),
        "start_price": start_price,
        "end_price": end_price,
        "years": years,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    fv = sub.add_parser("future-value", help="Compound growth of a lump sum plus monthly contributions")
    fv.add_argument("--principal", type=float, required=True)
    fv.add_argument("--contribution", type=float, required=True)
    fv.add_argument("--annual-rate", type=float, required=True)
    fv.add_argument("--years", type=float, required=True)

    rc = sub.add_parser("required-capital", help="Capital needed to sustain a target monthly income via a safe withdrawal rate")
    rc.add_argument("--target-monthly-income", type=float, required=True)
    rc.add_argument("--swr", type=float, required=True, help="Safe withdrawal rate, e.g. 0.04 for the 4%% rule")

    am = sub.add_parser("amortization", help="Payoff time and total interest for a fixed monthly payment")
    am.add_argument("--principal", type=float, required=True)
    am.add_argument("--annual-rate", type=float, required=True)
    am.add_argument("--monthly-payment", type=float, required=True)

    cc = sub.add_parser("convert-currency", help="Convert an amount using a rate the caller already sourced")
    cc.add_argument("--amount", type=float, required=True)
    cc.add_argument("--rate", type=float, required=True)

    cg = sub.add_parser("cagr", help="Compound annual growth rate between two prices over N years")
    cg.add_argument("--start-price", type=float, required=True)
    cg.add_argument("--end-price", type=float, required=True)
    cg.add_argument("--years", type=float, required=True)

    args = parser.parse_args()

    if args.command == "future-value":
        result = future_value(args.principal, args.contribution, args.annual_rate, args.years)
    elif args.command == "required-capital":
        result = required_capital(args.target_monthly_income, args.swr)
    elif args.command == "amortization":
        result = amortization(args.principal, args.annual_rate, args.monthly_payment)
    elif args.command == "convert-currency":
        result = convert_currency(args.amount, args.rate)
    elif args.command == "cagr":
        result = cagr(args.start_price, args.end_price, args.years)
    else:
        parser.error(f"unknown command: {args.command}")
        return

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stdout)
        sys.exit(0)
