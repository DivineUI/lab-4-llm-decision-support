# SUMMARY_PROMPT
SUMMARY_PROMPT = "Summarize this loan application:\n\n{letter}"

# EXTRACT_PROMPT
EXTRACT_PROMPT = """Extract the following fields from the loan application letter below and return ONLY a JSON object with exactly these keys:
applicant_name (string)
amount_ghs (number)
purpose (string)
monthly_profit_ghs (number or null)
has_collateral_or_guarantor (boolean)
repayment_months (number or null)
If a field is not stated in the letter, use null. Do not guess or infer a value that is not explicitly stated.
Example:
Letter:
"My name is Divine Uwase. I run a medium bakery in Accra and I am requesting GHS 10,000 to buy a new oven. I make about GHS 1000 profit a month. I have no guarantor yet but I am hoping to find one. I can repay over 10 months."
JSON:
{{"applicant_name": "Divine Uwase", "amount_ghs": 10000, "purpose": "buy a new oven", "monthly_profit_ghs": 1000, "has_collateral_or_guarantor": false, "repayment_months": 10}}
Now extract from this letter:
{letter}
JSON:"""

# BRIEF_PROMPT
BRIEF_PROMPT = """Given the loan application letter and the extracted data below, produce a decision-support brief with exactly these four sections:
1. Strengths (bullet points, grounded only in the letter/data)
2. Risks / Red flags (bullet points)
3. Missing information the officer should request before deciding
4. Suggested next step — choose ONE of: "invite for interview", "request documents", "flag for senior review". Do NOT say "approve" or "reject" — the final decision is made by a human loan officer, not by you.

Letter:
{letter}

Extracted data (JSON):
{extracted_json}

Brief:"""

