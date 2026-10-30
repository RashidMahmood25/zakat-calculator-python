# Zakat Calculator (Python)
A small command-line tool that estimates Zakat on cash, bank savings, gold, silver and trade goods, after subtracting debts, at the standard rate of 2.5%.
## How to run
python3 zakat_calculator.py
Answer the prompts (all amounts in PKR; enter 0 where not applicable).
## Nisab note (important)
The script uses the commonly quoted nisab thresholds as defaults only: gold 87.48 grams and silver 612.36 grams, valued at the rates you enter. Gold/silver rates change daily, so check the current local rate before calculating. The nisab shown is the lower of the gold and silver values — the more cautious, commonly used position.
This is an educational estimate, not a religious ruling. For complex cases (business stock, agricultural produce, different kinds of debt), ask a qualified scholar.
## What was practiced
- Input validation (numbers, no negatives)
- Separating calculation logic from user input
- Clear labelling of assumptions (nisab, rates) in code and docs
