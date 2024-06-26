from fastapi import (
    APIRouter,
    File,
    UploadFile,
    Query,
    Body,
    Path,
    Depends,
    HTTPException,
)
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
import uvicorn
from datetime import datetime
import os
from ..database import SessionLocal, engine, get_db
from .. import crud, models, schemas
from sqlalchemy.orm import Session

router: APIRouter = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.get("/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items