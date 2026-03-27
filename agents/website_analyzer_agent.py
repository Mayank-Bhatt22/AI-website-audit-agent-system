from services.llm_service import run_llm


def run_website_analyzer(url, website_data):

    prompt = f"""
ROLE:
You are a Website Analysis Agent responsible for extracting structured information from websites.

INPUT:
URL: {url}

WEBSITE DATA:
{website_data}

OUTPUT FORMAT (JSON):

{{
  "website_title": "",
  "meta_description": "",
  "headings": [],
  "content_summary": "",
  "navigation_structure": [],
  "cta_elements": [],
  "forms_detected": [],
  "media_elements": [],
  "internal_links": [],
  "external_links": []
}}

Return ONLY valid JSON.
"""

    result = run_llm(prompt)

    return result