from config import client, MODEL


def run_technical_audit(website_data):

    prompt = f"""
ROLE:
You are a Technical Website Audit Agent specializing in SEO and performance.

INPUT WEBSITE DATA:
{website_data}

Analyze SEO, performance, and technical issues.

OUTPUT FORMAT:

Technical Score: (0-100)

Issues Found:
1. Issue
Description
Recommended Fix
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an SEO expert."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content