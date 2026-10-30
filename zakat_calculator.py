#!/usr/bin/env python3
"""Zakat calculator (simple, educational).
Asks for cash, bank balance, gold, silver and trade goods, subtracts
debts, then applies the standard 2.5% rate on wealth above the nisab.
Nisab note: this script uses the commonly quoted nisab values as
DEFAULTS only (gold: 87.48 grams, silver: 612.36 grams, valued at the
rates you enter). Gold/silver market rates change daily, so always
check the current local rate and enter it yourself. This tool does not
replace a scholar's ruling for complex cases (e.g. business stock,
agricultural produce, or debts of different kinds).
"""
GOLD_NISAB_GRAMS = 87.48
SILVER_NISAB_GRAMS = 612.36
ZAKAT_RATE = 0.025
def ask_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip().replace(",", ""))
            if value < 0:
                print("  Please enter 0 or a positive number.")
                continue
            return value
        except ValueError:
            print("  Please enter a number.")
def main():
    print("=== Zakat Calculator ===")
    print("All amounts in PKR. Enter 0 where not applicable.\n")
    cash = ask_float("Cash in hand (PKR): ")
    bank = ask_float("Bank balance (PKR): ")
    gold_grams = ask_float("Gold owned (grams, 0 if none): ")
    gold_rate = ask_float("Current gold rate per gram (PKR): ") if gold_grams else 0.0
    silver_grams = ask_float("Silver owned (grams, 0 if none): ")
    silver_rate = ask_float("Current silver rate per gram (PKR): ") if silver_grams else 0.0
    trade_goods = ask_float("Trade goods / stock value (PKR): ")
    debts = ask_float("Debts owed (PKR): ")
    gold_value = gold_grams * gold_rate
    silver_value = silver_grams * silver_rate
    net_wealth = cash + bank + gold_value + silver_value + trade_goods - debts
    nisab_gold = GOLD_NISAB_GRAMS * gold_rate if gold_rate else 0.0
    nisab_silver = SILVER_NISAB_GRAMS * silver_rate if silver_rate else 0.0
    nisab = min(v for v in (nisab_gold, nisab_silver) if v > 0) if (nisab_gold or nisab_silver) else 0.0
    print("\n--- Result ---")
    print(f"Gold value:   PKR {gold_value:,.2f}")
    print(f"Silver value: PKR {silver_value:,.2f}")
    print(f"Net wealth (after debts): PKR {net_wealth:,.2f}")
    if nisab:
        print(f"Nisab (lower of gold/silver value): PKR {nisab:,.2f}")
    if net_wealth > 0 and nisab and net_wealth >= nisab:
        print(f"Zakat due (2.5%): PKR {net_wealth * ZAKAT_RATE:,.2f}")
    elif net_wealth <= 0:
        print("Zakat due: PKR 0 (net wealth is zero or negative).")
    else:
        print("Zakat due: PKR 0 (net wealth is below nisab).")
    print("\nNote: rates change daily — re-check gold/silver rates before paying.")
if __name__ == "__main__":
    main()
