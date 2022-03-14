from datetime import date, datetime
from typing import Optional, List

from pydantic import BaseModel

# AnnualEarning
class AnnualEarningBase(BaseModel):
    fisical_date_endig: datetime
    reported_eps: float


class AnnualEarningsCreate(AnnualEarningBase):
    pass


class AnnualEarning(AnnualEarningBase):
    id: int
    compani_id: int

    class Config:
        orm_mode = True


# Quarterly Earnings
class QuarterlyEarningsBase(AnnualEarningBase):
    estimated_eps: float
    surprise: float
    surprice_percentage: float


class QuarterlyEarningsCreate(QuarterlyEarningsBase):
    pass


class QuarterlyEarnings(QuarterlyEarningsBase):
    id: int
    comani_id: int

    class Config:
        orm_mode = True


# Sector
class SectorBase(BaseModel):
    name: str


class SectorCreate(BaseModel):
    pass


class Sector(SectorBase):
    id: int

    class Config:
        orm_mode = True


# Country
class CountryBase(BaseModel):
    name: str


class CountryCreate(CountryBase):
    pass


class Country(CountryBase):
    id: int

    class Config:
        orm_mode = True


# Company
class CompanyBase(BaseModel):
    symbol: str
    description: str


class CompanyCreate(CompanyBase):
    country: CountryBase
    sector: SectorBase
    annual_earnings: List[AnnualEarningBase] = []
    quarterly_earnings: List[QuarterlyEarningsBase] = []


class Company(CompanyCreate):
    id: int

    class Config:
        orm_mode = True


class CompanyResponseModel(Company):
    sector: Sector
    country: Country
    annual_earnings: AnnualEarning
    quarterly_earnings: QuarterlyEarnings
