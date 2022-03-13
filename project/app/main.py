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
# model
from app.models import Company

from app.models import Base
# data complilations
from app.data_transform_n_load.company_load import  LoadCompany

app = FastAPI(title=APP_TITLE, description=PROJECT_DESCRIPTION)

Base.metadata.create_all(bind=engine)


@app.post("/aggregate/{symbol}")
def aggregate_symbol(symbol: str, db: Session= Depends(get_db)):
    company_load = LoadCompany()
    _cd = company_load.get_company_data(symbol=symbol)
    #_earnings = company_load.get_company_quarterly_earnings(
    #    _cd['EARNINGS']
    # )
    import pdb;pdb.set_trace()
    

@app.get("/sumary/{symbol}")
async def get_company_sumary(symbol: str):
    pass


@app.get("/info")
async def info(settings: APPSettings = Depends(get_settings)):
    return {"app_name": settings.app_name, "admin_email": settings.admin_email}
