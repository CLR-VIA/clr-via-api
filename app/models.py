from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    JSON,
    Float,
    Text,
    Uuid,
)
from sqlalchemy.orm import Relationship
from .database import Base
import uuid


class User(Base):
    __tablename__: str = "users"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = Relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__: str = "items"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True)
    description = Column(String)
    owner_id = Column(Uuid, ForeignKey("users.id"))
    owner = Relationship("User", back_populates="items")
