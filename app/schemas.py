from pydantic import BaseModel, Field, validate_email, field_validator
from datetime import date
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


class ProjectBase(BaseModel):
    company: str
    title: str
    start_date: date
    end_date: date | None
    description: list[str] | None
    on_going: bool


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: UUID
    user_id: UUID

    class Config:
        from_attributes = True


class ExperienceBase(BaseModel):
    employer: str
    title: str
    location: str
    start_date: date
    end_date: date | None
    description: list[str]
    on_going: bool


class ExperienceCreate(ExperienceBase):
    pass


class Experience(ExperienceBase):
    id: UUID
    user_id: UUID

    class Config:
        from_attributes = True


class EducationBase(BaseModel):
    school_name: str
    major: str
    minor: str | None
    graduation_date: str
    description: list[str]


class EducationCreate(EducationBase):
    pass


class Education(EducationBase):
    id: UUID
    user_id: UUID

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str
    first_name: str
    middle_name: str | None
    last_name: str
    phone_number: str | None
    linkedin: str | None
    github: str | None
    portfolio: str | None
    summary: str | None
    skills: list[str] | None
    certifications: list[str] | None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID
    projects: list[Project] = []
    experience: list[Experience] = []
    education: list[Education] = []

    class Config:
        from_attributes = True
