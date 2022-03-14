# Models
from app.models import Company, QuarterlyEarnings
# Schemas
from app.schemas import CompanyResponseModel
# DB Session
from sqlalchemy.orm import Session
# Extractor
from app.data_extraction.company import get_all_company_data
# company  creator 
from app.data_transform_n_load.company_load import LoadCompany
# constants
from app.constants import(
    SYMBOL_KEY,
    OVERVIEW_FUNCTION
)

class CompanySolver():
    def __init__(self, company_symbol:str):
        self.company_symbol = company_symbol
    
    def get_company_data(self, db: Session)->CompanyResponseModel:
        company_summary = {}
        company = db.query(Company).filter(
            Company.symbol==self.company_symbol
        ).first()
        if not company:
            all_company_data = get_all_company_data(symbol=self.company_symbol)
            load_company = LoadCompany()
            load_company.set_commpany_data(
                all_company_data=all_company_data,
                db=db
            )
            load_company.set_all_company_earning_anual(all_company_data=all_company_data, db=db)
            load_company.set_all_company_earning_quarterlies(all_company_data=all_company_data, db=db)
        response_model  = {
            'sector': company.sector.name,
            'country': company.country.name,
            'symbol': company.symbol,
            'description': company.description,
            'quarterly_earnings': company.quarterly_earnings,
            'annual_earnings': company.annual_earnings
        }        
        return response_model
