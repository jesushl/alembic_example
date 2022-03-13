# loaders
from sqlalchemy import over
from app.data_extraction import company as company_loader
# models 
from app.models import(  
    Company, 
    Country, 
    AnnualEarning, 
    QuarterlyEarnings,
    Sector
    )
# constants
from app.constants import (
    EARNINGS_FUNCTION,
    OVERVIEW_FUNCTION,
    SYMBOL_KEY,
    ANNUAL_EARNINGS_KEY,
    QUARTERLY_EARNINGS_KEY,
    quarterly_earnings_key,
    annual_earnings_key,
    fiscal_date_ending_key, 
    reportedEPS_key,
    reported_date_key,
    surprice_key, 
    surprice_percentage_key,
    description_key
)

class LoadCompany():

    def get_company_data(self, symbol: str) -> dict:
        company_data = dict()
        company_overview = company_loader.get_company_overview(
            symbol=symbol
        )
        company_earnings = company_loader.get_company_earnings(
            symbol=symbol
        )
        company_data[EARNINGS_FUNCTION] = company_earnings
        company_data[OVERVIEW_FUNCTION] = company_overview
        return company_data

    def get_company_overview(self, overview: dict)->bool:
            symbol = overview[SYMBOL_KEY]
            company = Company.query.get(
                Company.symbol==symbol
            )
            if not company:
                comp_instance = Company(
                    symbol=symbol,
                    description = overview[description_key],
                    
                )

    def get_company_quarterly_earnings(self, earnings: dict)->bool:
        symbol = earnings[SYMBOL_KEY]
        quarterly_earnings = earnings[QUARTERLY_EARNINGS_KEY]
        company = Company.query.filter(
            Company.symbol==symbol
        ).first()
        if not company:
           return False 
        else:
            q_earnings_lamb = lambda dirty_earning: QuarterlyEarnings(
                fiscal_date_ending=dirty_earning[fiscal_date_ending_key],
                reported_eps = dirty_earning[reportedEPS_key],
                compani_id = company.id
            )
            q_earnings = list(map(q_earnings_lamb, quarterly_earnings))
            import pdb; pdb.set_trace()
