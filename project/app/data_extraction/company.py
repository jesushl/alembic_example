import requests

# settings
from app.settings import get_settings

# store in cache
from functools import lru_cache

# api url
from app.constants import (
    ALPHAVANTAGE_API_URL,
    EARNINGS_FUNCTION,
    OVERVIEW_FUNCTION
)

settings = get_settings()


@lru_cache()
def get_function_link(symbol: str, function: str):
    return ALPHAVANTAGE_API_URL.format(
        symbol=symbol, 
        function=function, 
        ALPHAVANTAGE_KEY=settings.alphavantage_key
    )


def get_company_overview(symbol: str) -> dict:
    function = OVERVIEW_FUNCTION
    url = get_function_link(symbol=symbol, function=function)
    response = requests.get(url)
    return response.json()


def get_company_earnings(symbol: str) -> dict:
    function = EARNINGS_FUNCTION
    api_url = get_function_link(symbol=symbol, function=function)
    response = requests.get(api_url)
    return response.json()


def get_all_company_data(symbol: str) -> dict:
    all_company_data = dict()
    company_overview = get_company_overview(
        symbol=symbol
    )
    company_earnings = get_company_earnings(
        symbol=symbol
    )
    all_company_data[EARNINGS_FUNCTION] = company_earnings
    all_company_data[OVERVIEW_FUNCTION] = company_overview
    return all_company_data
