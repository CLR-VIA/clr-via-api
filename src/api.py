from fastapi import FastAPI, APIRouter, File, UploadFile, Query, Body, Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
import uvicorn
import routers
from datetime import datetime

# FastAPI Config
clr_via_link = "https://github.com/angel-badillo-hernandez/codename-cv"
title: str = "CLR VIA API"
description: str = f"""
<a href="{clr_via_link}"><img href="/" src="public/logo.png" height=256px></a>
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


@app.get("/", tags=["/"])
def docs_redirect():
    return RedirectResponse(url="/index.html")  # change to this

app.mount("/", StaticFiles(directory="../public", html=True), name="public")

app.include_router(routers.example.router)
