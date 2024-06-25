from fastapi import APIRouter, HTTPException, Body, Path, Query, File

router:APIRouter = APIRouter(
    prefix="/example",
    tags=["Example"],
)

@router.get("/")
def get_example():
    return 1