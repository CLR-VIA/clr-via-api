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
from uuid import UUID, uuid4

router: APIRouter = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db))-> dict[str,str]:
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return {"id": str(crud.create_user(db=db, user=user).id)}


@router.get("/", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = None, db: Session = Depends(get_db))-> list[schemas.User]:
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def get_user_by_id(user_id: UUID, db: Session = Depends(get_db))-> schemas.User:
    db_user = crud.get_user_by_id(db, user_id=user_id)
        
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found or was deleted")
    return db_user

@router.get("/{user_id}/email")
def get_user_email_by_id(user_id:UUID, db:Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
        
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found or was deleted")
    return {"email": db_user.email}

@router.delete("/{user_id}")
def delete_user(user_id: UUID, db:Session = Depends(get_db))-> dict[str,str]:
    db_user = crud.get_user_by_id(db, user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found or was deleted")
    
    crud.delete_user(db, user_id)

    return {"id": str(db_user.id)}

# @router.post("/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: UUID, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)
