from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship

from app.database import Base

# Company Database model
class Country(Base):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    companies = relationship("Company", back_populates="country")


class Sector(Base):
    __tablename__ = "sector"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    companies = relationship("Company", back_populates="sector")


class AnnualEarning(Base):
    __tablename__ = "anual_earning"
    id = Column(Integer, primary_key=True, index=True)
    fiscal_date_ending = Column(Date)
    reported_eps = Column(Float)
    company_id = Column(Integer, ForeignKey("company.id"))
    company = relationship("Company", back_populates="annual_earnings")


class QuarterlyEarnings(Base):
    __tablename__ = "quarterly_earning"
    id = Column(Integer, primary_key=True, index=True)
    fiscal_date_ending = Column(Date)
    reported_eps = Column(Float)
    estimated_eps = Column(Float)
    surprise = Column(Float)
    surprice_percentage = Column(Float)
    company_id = Column(Integer, ForeignKey("company.id"))
    company = relationship("Company", back_populates="quarterly_earnings")

class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True)
    description = Column(String)
    country_id = Column(Integer, ForeignKey('country.id'))
    country = relationship("Country", back_populates="companies")
    sector_id = Column(Integer, ForeignKey('sector.id'))
    sector = relationship("Sector", back_populates="companies")

    annual_earnings = relationship("AnnualEarning", back_populates="company")
    quarterly_earnings = relationship("QuarterlyEarnings", back_populates="company")
