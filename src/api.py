from fastapi import FastAPI, APIRouter, File, UploadFile, Query, Body, Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
import uvicorn
from routers import example

app:FastAPI = FastAPI()

@app.get("/", tags=["/"])
def docs_redirect():
    return RedirectResponse("/docs")

app.include_router(example.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
       uvicorn.run("api:app", port=8080, reload=True)