from config import client, MODEL


def run_business_analysis(website_data, technical_report):

    prompt = f"""
ROLE:
You are a Business Strategy Analysis Agent.

INPUT:
Website Data:
{website_data}

Technical Audit:
{technical_report}

Analyze marketing and business strategy.

OUTPUT FORMAT:

Business Score: (0-100)

Strengths:
- point

Weaknesses:
- point

Business Recommendations:
1. recommendation
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a business consultant."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content