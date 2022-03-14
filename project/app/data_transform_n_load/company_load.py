# DB Session
from sqlalchemy.orm import Session
# loaders
from pytest import Session
from app.data_extraction import company as company_loader
# models 
from app.models import(  
    Company, 
    Country, 
    AnnualEarning, 
    QuarterlyEarnings,
    Sector,
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
    surprise_key, 
    surprise_percentage_key,
    description_key,
    country_key,
    industry_key,
    sector_key,
    symbol_overview_key,
    industry_key,
    sector_key,
    estimated_eps_key,
    symbol_earnings_key
)

class LoadCompany():
    
    def set_commpany_data(self, all_company_data: dict, db: Session)->Company:
        company_data = all_company_data[OVERVIEW_FUNCTION]
        _company_symbol=company_data[country_key]
        # Doble check if company exist
        company = db.query(Company).filter(Company.symbol==_company_symbol).first()
        if not company:
            _country_name = company_data[country_key]
            country = db.query(Country).filter(Country.name==_country_name).first()
            if not  country:
                country = Country(name=_country_name)
                db.add(country)
                db.commit()
                db.refresh(country)
            _sector_name = company_data[sector_key]
            sector = db.query(Sector).filter(Sector.name==_sector_name).first()
            if not sector:
                sector = Sector(name=_sector_name)
                db.add(sector)
                db.commit()
                db.refresh(sector)
            company = Company(
                symbol=company_data[symbol_overview_key],
                description=company_data[description_key],
                country_id=country.id,
                sector_id=sector.id
            )
            db.add(company)
            db.commit()
            db.refresh(company) 
        return company  
        

    def set_all_company_earning_quarterlies(self, all_company_data: dict, db: Session,)->bool:
            dirty_quarterlies = all_company_data[EARNINGS_FUNCTION][QUARTERLY_EARNINGS_KEY]
            symbol = all_company_data[EARNINGS_FUNCTION][symbol_earnings_key]
            company = db.query(Company).filter(
                Company.symbol==symbol
            ).first()
            if not company:
                company = self.set_commpany_data(all_company_data)
            to_quarterly = lambda dirty_quarterlie: QuarterlyEarnings(
                fiscal_date_ending=dirty_quarterlie[fiscal_date_ending_key],
                reported_eps=float(dirty_quarterlie[reportedEPS_key]),
                estimated_eps=float(dirty_quarterlie[estimated_eps_key]),
                surprise = float(dirty_quarterlie[surprise_key]),
                surprise_percentage=float(dirty_quarterlie[surprise_percentage_key]),
                company_id = company.id
            )
            quarterly_objs = map(to_quarterly, dirty_quarterlies)
            _ = list(map(db.add, quarterly_objs))
            import pdb; pdb.set_trace()
            db.commit()
            return True

    def set_all_company_earning_anual(self, all_company_data: dict, db: Session)->bool:
        dirty_annuals = all_company_data[EARNINGS_FUNCTION][ANNUAL_EARNINGS_KEY]
        symbol = all_company_data[EARNINGS_FUNCTION][symbol_earnings_key]
        company = db.query(Company).filter(
                Company.symbol==symbol
            ).first()
        if not company:
            company = self.set_commpany_data(all_company_data, db=db)
        to_annual = lambda dirty_annual: AnnualEarning(
            fiscal_date_ending=dirty_annual[fiscal_date_ending_key],
            reported_eps=float(dirty_annual[reportedEPS_key]),
            company_id=company.id
        )
        annual_objs = map(to_annual, dirty_annuals)
        _ = list(map(db.add, annual_objs))
        db.commit()
        return True
