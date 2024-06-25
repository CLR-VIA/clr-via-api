from fastapi import FastAPI, APIRouter, File, UploadFile, Query, Body, Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
import uvicorn
from .routers import example
from datetime import datetime
import os
from . import database_manager

# BASE PATH
BASE_DIR = os.path.dirname(__file__)

# FastAPI Config
clr_via_link = "https://github.com/angel-badillo-hernandez/codename-cv"
title: str = "CLR VIA API"
description: str = f"""
<a href="{clr_via_link}"><img href="/" src="/logo.png" height=256px></a>
## Welcome to the CLR VIA API!
Brief overview here...
<br/>
<br/>
Copyright ©️ {datetime.now().year}. All Rights Reserved.
"""
summary: str = (
    "CLR VIA API for login, registration, and other services of CLR VIA web app."
)
terms_of_service: str = clr_via_link
version: str = "0.0.1"
contact: dict = {"name": "CLR VIA", "url": clr_via_link, "email": "admin@email.com"}
# TODO: Update this when deploying app
# license_info:dict = {
#     "name": "N/A",
#     "url": None
# }

app: FastAPI = FastAPI(
    title=title,
    description=description,
    terms_of_service=terms_of_service,
    summary=summary,
    version=version,
    contact=contact,
    # license_info=license_info,
)

# Include API Routers to FastAPI app
app.include_router(example.router)

@app.get("/", tags=["/"])
def docs_redirect():
    return RedirectResponse(url="/index.html")  # change to this

# TODO: Database connection is not working, fix
@app.get("/db-test")
def d():
    database_manager.db_test()
    return {"hi": 11}

# Mount static files directory
app.mount("/", StaticFiles(directory=os.path.join(BASE_DIR, "public"), html=True), name="public")