from pydantic import BaseModel
from typing import List


class WebsiteAnalysis(BaseModel):
    website_title: str
    meta_description: str
    headings: List[str]
    content_summary: str
    navigation_structure: List[str]
    cta_elements: List[str]
    forms_detected: List[str]
    media_elements: List[str]
    internal_links: List[str]
    external_links: List[str]


class TechnicalIssue(BaseModel):
    issue_name: str
    description: str
    recommended_fix: str


class TechnicalAudit(BaseModel):
    technical_score: int
    issues_found: List[TechnicalIssue]


class BusinessAnalysis(BaseModel):
    business_score: int
    strengths: List[str]
    weaknesses: List[str]
    recommendations: List[str]


class StrategyReport(BaseModel):
    overall_score: int
    critical_issues: List[str]
    immediate_fixes: List[str]
    six_month_strategy: List[str]
    twelve_month_growth: List[str]
    ai_opportunities: List[str]