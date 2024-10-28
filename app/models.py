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
    Date,
    ARRAY,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Relationship
from .database import Base
import uuid


class User(Base):
    __tablename__: str = "users"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    first_name = Column(String)
    middle_name = Column(String, nullable=True)
    last_name = Column(String)
    phone_number = Column(String, nullable=True)
    linkedIn = Column(String, nullable=True)
    gitHub = Column(String, nullable=True)
    portfolio = Column(String, nullable=True)
    summary = Column(String, nullable=True)
    workExperience = Column(JSONB, nullable=True)
    education = Column(JSONB, nullable=True)
    skills = Column(String, nullable=True)
    projects = Column(JSON, nullable=True)
    certifications = Column(String, nullable=True)

    # workExperiences = Relationship("WorkExperience", back_populates="workExperiences")


# class WorkExperience(Base):
#     __tablename__: str = "workExperience"

#     id = Column(Uuid, primary_key=True, default=uuid.uuid4)
#     employer = Column(String)
#     title = Column(String)
#     location = Column(String)
#     start_date = Column(Date)
#     end_date = Column(Date)
#     description = Column(JSONB)
#     on_going = Column(Boolean)

#     user_id = Column(Uuid, ForeignKey("users.id"))
#     user = Relationship("User", back_populates="workExperiences")


# class Education(Base):
#     __tablename__: str = "education"

#     id = Column(Uuid, primary_key=True, default=uuid.uuid4)
#     school_name = Column(String)
#     major = Column(String)
#     graduation_date = Column(Date)
#     description = Column(JSONB)

#     user_id = Column(Uuid, ForeignKey("users.id"))
#     user = Relationship("User", back_populates="workExperiences")


# # Example class
# class Item(Base):
#     __tablename__: str = "items"

#     id = Column(Uuid, primary_key=True, default=uuid.uuid4)
#     title = Column(String, index=True)
#     description = Column(String)
#     owner_id = Column(Uuid, ForeignKey("users.id"))
#     owner = Relationship("User", back_populates="items")
