import os

APP_TITLE = "Companies data scraping"
PROJECT_DESCRIPTION = """This application is an API  works to provide information about companies,
                                                        as name, description, country, sector and lates annual earnings per share and latest 
                                                        quarterly earnings per share
                                                        """

ALPHAVANTAGE_API_URL = "https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={ALPHAVANTAGE_KEY}"

EARNINGS_FUNCTION = "EARNINGS"
OVERVIEW_FUNCTION = "OVERVIEW"
SYMBOL_KEY = 'symbol'
ANNUAL_EARNINGS_KEY='annualEarnings'
QUARTERLY_EARNINGS_KEY='quarterlyEarnings'
## ALPHAVANTAGE API KEYS
annual_earnings_key = "annualEarnings"
quarterly_earnings_key = "quarterlyEarnings"
fiscal_date_ending_key="fiscalDateEnding"
reportedEPS_key='reportedEPS'
reported_date_key='reportedDate'
surprice_key='surprice'
surprice_percentage_key='surpricePercentaje'
name_key = 'name'
description_key = 'Description',
country_key = 'Country'
industry_key = 'Industry'
sector_key = 'Sector'

# ENV VARS
ALPHAVANTAGE_KEY = os.getenv("ALPHAVANTAGE_KEY")

DATABASE_URL=os.environ.get("DATABASE_URL", "sqlite:///./sql_app.db")
