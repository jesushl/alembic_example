import requests
# store in cache
from functools import lru_cache 
# app settings 
from app.main import get_settings
# api url 
from app.constants import (
    ALPHAVANTAGE_API_URL, 
    EARNINGS_FUNCTION, 
    OVERVIEW_FUNCTION,
    annual_earnings, 
    quarterly_earnings
)

settings = get_settings()

@lru_cache()
def get_function_link(symbol: str, function: str):
    return ALPHAVANTAGE_API_URL.format(
        symbol=symbol,
        function=function,
        ALPHAVANTAGE_KEY=settings.ALPHAVANTAGE_KEY
    )


def get_company_overview(symbol: str)->dict:
    function = OVERVIEW_FUNCTION

def get_company_earnings(symbol: str)->dict:
    function = EARNINGS_FUNCTION
    api_url = get_function_link(symbol=symbol, function=function)
    response = requests.get(api_url)
    return response