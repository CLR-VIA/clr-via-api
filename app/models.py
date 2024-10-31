from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    Text,
    Uuid,
    Date,
)
from sqlalchemy.dialects.postgresql import JSONB, ARRAY, JSON
from sqlalchemy.orm import Relationship
from .database import Base
import uuid


class User(Base):
    __tablename__: str = "users"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    first_name = Column(String)
    middle_name = Column(String, nullable=True)
    last_name = Column(String)
    phone_number = Column(String, nullable=True)
    linkedin = Column(String, nullable=True)
    github = Column(String, nullable=True)
    portfolio = Column(String, nullable=True)
    summary = Column(String, nullable=True)
    skills = Column(ARRAY(String, dimensions=1), nullable=True)
    certifications = Column(ARRAY(String, dimensions=1), nullable=True)

    experience = Relationship("WorkExperience", back_populates="experience")
    education = Relationship("Education", back_populates="education")
    projects = Relationship("Project", back_populates="project")


class Project(Base):
    __tablename__: str = "project"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    company = Column(String)
    title = Column(String)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    description = Column(ARRAY(String, dimensions=1), nullable=True)
    on_going = Column(Boolean)

    user_id = Column(Uuid, ForeignKey("users.id"))
    user = Column("User", back_populates="projects")


class Experience(Base):
    __tablename__: str = "work_experience"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    employer = Column(String)
    title = Column(String)
    location = Column(String)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    description = Column(ARRAY(String, dimensions=1), nullable=True)
    on_going = Column(Boolean)

    user_id = Column(Uuid, ForeignKey("users.id"))
    user = Relationship("User", back_populates="experience")


class Education(Base):
    __tablename__: str = "education"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    school_name = Column(String)
    major = Column(String)
    minor = Column(String, nullable=True)
    graduation_date = Column(Date)
    description = Column(ARRAY(String, dimensions=1))

    user_id = Column(Uuid, ForeignKey("users.id"))
    user = Relationship("User", back_populates="education")


# # Example class
# class Item(Base):
#     __tablename__: str = "items"

#     id = Column(Uuid, primary_key=True, default=uuid.uuid4)
#     title = Column(String, index=True)
#     description = Column(String)
#     owner_id = Column(Uuid, ForeignKey("users.id"))
#     owner = Relationship("User", back_populates="items")
