from fastapi import APIRouter, HTTPException, Body, Path, Query, File

router:APIRouter = APIRouter(
    prefix="/example",
    tags=["Example"],
)

@router.get("/")
async def get_example():
    return {"Hello": "There"}