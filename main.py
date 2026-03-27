from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tools.scraper import scrape_website
from agents.website_analyzer_agent import run_website_analyzer
from agents.technical_audit_agent import run_technical_audit
from agents.business_analysis_agent import run_business_analysis
from agents.strategy_agent import generate_final_strategy

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "AI Website Audit System Running"}


@app.get("/audit")
def audit(url: str):

    try:
        print("Step 1: Scraping website...")
        website_data = scrape_website(url)

        print("Step 2: Running Website Analyzer Agent...")
        analyzer = run_website_analyzer(url, website_data)

        print("Step 3: Running Technical Audit Agent...")
        tech_report = run_technical_audit(analyzer)

        print("Step 4: Running Business Analysis Agent...")
        business_report = run_business_analysis(analyzer, tech_report)

        print("Step 5: Running Strategy Agent...")
        final_strategy = generate_final_strategy(
            analyzer,
            tech_report,
            business_report
        )

        return {
            "website_analysis": analyzer,
            "technical_report": tech_report,
            "business_report": business_report,
            "final_strategy": final_strategy
        }

    except Exception as e:
        return {"error": str(e)}
    