from calendar import c
from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel

from app.models import AnnualEarning, Company


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
    companies: list["Company"] = []

    class Config:
        orm_mode = True


# Country
class CountryBase(BaseModel):
    name: str


class CountryCreate(CountryBase):
    pass


class Country(CountryBase):
    id: int
    companies: list[int] = []

    class Config:
        orm_mode = True


# Company
class CompanyBase(BaseModel):
    symbol: str
    description: str


class CompanyCreate(CompanyBase):
    country: CountryBase
    sector: SectorBase
    annual_earnings: list["AnnualEarningBase"] = []
    quarterly_earnings: list["QuarterlyEarningsBase"] = []


class Company(CompanyCreate):
    id: int

    class Config:
        orm_mode = True
