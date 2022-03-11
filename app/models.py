from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship

from .database import Base

# Company Database model
class Country(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    companies = relationship("Company", back_populates="country")


class Sector(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    companies = relationship("Company", back_populates="sector")


class AnnualEarning(Base):
    __tablename__ = "anual_earning"
    id = Column(Integer, primary_key=True, index=True)
    fiscal_date_ending = Column(Date)
    reported_eps = Column(Float)
    compani_id = Column(Integer, ForeignKey("country.id"))


class QuarterlyEarnings(Base):
    __tablename__ = "anual_earning"
    id = Column(Integer, primary_key=True, index=True)
    fiscal_date_ending = Column(Date)
    reported_eps = Column(Float)
    estimated_eps = Column(Float)
    surprise = Column(Float)
    surprice_percentage = Column(Float)
    compani_id = Column(Integer, ForeignKey("country.id"))


class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True)
    description = Column(String)
    country = relationship("Country", back_populates="companies")
    sector = relationship("Sector", back_populates="companies")
    annual_earnings = relationship("AnnualEarning", back_populates="compani_id")
    annual_earnings = relationship("QuarterlyEarnings", back_populates="compani_id")
