from config import client, MODEL


def generate_final_strategy(website_data, tech_report, business_report):

    prompt = f"""
ROLE:
You are a Strategic AI Consultant.

INPUT:

Website Data:
{website_data}

Technical Audit:
{tech_report}

Business Analysis:
{business_report}

Generate final strategy.

OUTPUT FORMAT:

Website Overall Score: (0-100)

Critical Issues:
- issue

Immediate Fixes:
- fix

6 Month Strategy:
- strategy

12 Month Growth Plan:
- strategy

AI Opportunities:
- chatbot
- automation
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a strategic consultant."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content