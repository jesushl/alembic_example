from multiprocessing.connection import wait
from fastapi import FastAPI, Depends

# settings
from .settings import APPSettings, get_settings

# description
from .constants import PROJECT_DESCRIPTION, APP_TITLE
# database
from app.database import  engine, get_db   
# db session
from sqlalchemy.orm import Session

from app.models import Base
# data complilations
from app.data_transform_n_load.company_load import  LoadCompany
from app.data_transform_n_load.company_solver import CompanySolver
app = FastAPI(title=APP_TITLE, description=PROJECT_DESCRIPTION)

Base.metadata.create_all(bind=engine)


@app.get("/sumary/{symbol}")
async def get_company_sumary(symbol: str, db: Session = Depends(get_db)):
    """
    This method receibe a symbol, if does not exits in our database
    go to  extract data, save it on our database and retunr the 
    stored data 
    """
    company_solver = CompanySolver(company_symbol=symbol)
    _  = company_solver.get_company_data(db)
    return _

@app.get("/")
async def info(settings: APPSettings = Depends(get_settings)):
    return {"app_name": settings.app_name, "admin_email": settings.admin_email}
