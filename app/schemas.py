from pydantic import BaseModel, Field, validate_email, field_validator
from uuid import UUID, uuid4

# class ItemBase(BaseModel):
#     title: str
#     description: str | None = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: UUID
#     owner_id: UUID

#     class Config:
#         from_attributes = True


# TODO: Update schemas to match sqlalchemy tables
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID
    is_active: bool
    # items: list[Item] = []

    class Config:
        from_attributes = True
