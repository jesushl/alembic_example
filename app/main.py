import imp
from multiprocessing.connection import wait
from fastapi import FastAPI, Depends

# settings
from .settings import APPSettings, get_settings

# description
from .constants import PROJECT_DESCRIPTION, APP_TITLE


app = FastAPI(title=APP_TITLE, description=PROJECT_DESCRIPTION)


@app.post("/aggregate/{symbol}")
async def aggregate_symbol(symbol: str):
    pass


@app.get("/sumary/{symbol}")
async def get_company_sumary(symbol: str):
    pass


@app.get("/info")
async def info(settings: APPSettings = Depends(get_settings)):
    return {"app_name": settings.app_name, "admin_email": settings.admin_email}
