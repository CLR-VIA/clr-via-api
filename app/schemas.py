from pydantic import BaseModel, Field, validate_email, field_validator
from uuid import UUID, uuid4


def uuid_validator(value: UUID) -> str:
    """Validator function used for Pydantic BaseModels with UUID field.

    Args:
        value (UUID): A value of type UUID.

    Returns:
        str: string representation of UUID.
    """
    if value:
        return str(value)
    else:
        return value


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: UUID
    owner_id: UUID

    _validate_id = field_validator("id")(uuid_validator)
    _validate_owner_id = field_validator("owner_id")(uuid_validator)

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID
    is_active: bool
    items: list[Item] = []

    _validate_id = field_validator("id")(uuid_validator)

    class Config:
        orm_mode = True


# class ExampleModel(BaseModel):
#     name:str = Field(description="Name of thing")
#     number:int = Field(description="Number of thing", ge=0)
