symbol = "IBM"

from operator import ipow
from unittest import result
from app.data_extraction.company import (
    get_function_link,
    get_company_overview,
    get_company_earnings,
    get_settings,
)

from app.constants import EARNINGS_FUNCTION, OVERVIEW_FUNCTION


def test_get_function_link():
    function = EARNINGS_FUNCTION
    expected_link_1 = (
        "https://www.alphavantage.co/query?function=EARNINGS&symbol=IBM&apikey=demo"
    )
    assert get_function_link(symbol, function) == expected_link_1
    function = OVERVIEW_FUNCTION
    expected_link_2 = (
        "https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo"
    )
    assert get_function_link(symbol, function) == expected_link_2


def test_get_company_overview():
    result = get_company_overview(symbol=symbol)
    assert result.get("Symbol") == symbol


def test_get_company_earnings():
    result = get_company_earnings(symbol=symbol)
    assert result.get("symbol") == symbol
