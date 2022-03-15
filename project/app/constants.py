import os

APP_TITLE = "Companies data tool from alphavantage.co"
PROJECT_DESCRIPTION = """This application is an API  works to provide information about companies,
 as name, description, country, sector and lates annual earnings per share and latest 
 quarterly earnings per share """

ALPHAVANTAGE_API_URL = "https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={ALPHAVANTAGE_KEY}"

EARNINGS_FUNCTION = "EARNINGS"
OVERVIEW_FUNCTION = "OVERVIEW"
SYMBOL_KEY = "symbol"
ANNUAL_EARNINGS_KEY = "annualEarnings"
QUARTERLY_EARNINGS_KEY = "quarterlyEarnings"
## ALPHAVANTAGE API KEYS
annual_earnings_key = "annualEarnings"
quarterly_earnings_key = QUARTERLY_EARNINGS_KEY
fiscal_date_ending_key = "fiscalDateEnding"
reportedEPS_key = "reportedEPS"
reported_date_key = "reportedDate"
estimated_eps_key = "estimatedEPS"
surprise_key = "surprise"
surprise_percentage_key = "surprisePercentage"
name_key = "name"
description_key = "Description"
country_key = "Country"
industry_key = "Industry"
sector_key = "Sector"
symbol_overview_key = "Symbol"
symbol_earnings_key = "symbol"
industry_key = "Industry"
sector_key = "Sector"

# ENV VARS
ALPHAVANTAGE_KEY = os.getenv("ALPHAVANTAGE_KEY")

DATABASE_URL = os.environ.get(
    "DATABASE_URL", 
    "sqlite:///./sql_app.db"
    ).replace(
        "postgres://", 
        "postgresql://"
    )
print(f"DATABASE URL in constants: {DATABASE_URL}")
