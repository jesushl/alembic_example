import imp
from multiprocessing.connection import wait
from fastapi import FastAPI , Depends
from functools import lru_cache
# settings
from .settings import APPSettings
# description
from .constants import PROJECT_DESCRIPTION
# data extraction
from .data_extraction.company import get_company_earnings

app = FastAPI(PROJECT_DESCRIPTION)


@app.post('/aggregate/{symbol}')
async def aggregate_symbol(symbol: str):
    pass 

@app.get('/sumary/{symbol}')
async def get_company_sumary(symbol: str):
    pass



@lru_cache()
def get_settings():
    return APPSettings()

@app.get("/info")
async def info(settings: APPSettings = Depends(get_settings)):
    _ = get_company_earnings('IBM')
    import pdb; pdb.set_trace()
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
