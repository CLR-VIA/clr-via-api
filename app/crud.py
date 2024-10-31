from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from hashlib import sha256
from uuid import UUID
from . import models, schemas


def get_user_by_id(db: Session, user_id: UUID):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if not user:
            raise ValueError("User not found.")
        return user
    except Exception as e:
        raise Exception(f"An error occurred while retrieving the user: {str(e)}")


def get_user_by_email(db: Session, email: str):
    try:
        user = db.query(models.User).filter(models.User.email == email).first()
        if not user:
            raise ValueError("User not found.")
        return user
    except Exception as e:
        raise Exception(
            f"An error occurred while retrieving the user by email: {str(e)}"
        )


def get_users(db: Session, skip: int = 0, limit: int = None):
    try:
        return db.query(models.User).offset(skip).limit(limit).all()
    except Exception as e:
        raise Exception(f"An error occurred while retrieving users: {str(e)}")


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = sha256(user.password.encode()).hexdigest()
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password,
        first_name=user.first_name,
        middle_name=user.middle_name,
        last_name=user.last_name,
        phone_number=user.phone_number,
        linkedin=user.linkedin,
        github=user.github,
        portfolio=user.portfolio,
        summary=user.summary,
        skills=user.skills,
        certifications=user.certifications,
    )

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise ValueError("A user with this email already exists.")
    except Exception as e:
        db.rollback()
        raise Exception(f"An error occurred while creating the user: {str(e)}")


def get_project_by_id(db: Session, project_id: UUID) -> models.Project:
    try:
        project = (
            db.query(models.Project).filter(models.Project.id == project_id).first()
        )
        if not project:
            raise ValueError("Project not found.")
        return project
    except Exception as e:
        raise Exception(f"An error occurred while retrieving the project: {str(e)}")


def get_projects(db: Session, skip: int = 0, limit: int = None) -> list[models.Project]:
    try:
        return (
            db.query(models.Project)
            .offset(skip)
            .limit(limit)
            .order_by(models.Project.start_date)
            .all()
        )
    except Exception as e:
        raise Exception(f"An error occurred while retrieving projects: {str(e)}")


def get_projects_by_user_id(
    db: Session, user_id: UUID, skip: int = 0, limit: int = None
) -> list[models.Project]:
    try:
        return (
            db.query(models.Project)
            .filter(models.Project.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .order_by(models.Project.start_date)
            .all()
        )
    except Exception as e:
        raise Exception(
            f"An error occurred while retrieving projects by user ID: {str(e)}"
        )


def create_project(db: Session, project: schemas.ProjectCreate, user_id: UUID):
    db_project: models.Project = models.Project(**dict(project), user_id=user_id)

    try:
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project
    except IntegrityError:
        db.rollback()
        raise ValueError(
            "An error occurred while creating the project: Duplicate entry."
        )
    except Exception as e:
        db.rollback()
        raise Exception(f"An error occurred while creating the project: {str(e)}")


def remove_project(db: Session, project_id: UUID):
    project = get_project_by_id(db, project_id)

    try:
        if project:
            db.delete(project)
            db.commit()
        else:
            raise ValueError("Project does not exist")
    except Exception as e:
        db.rollback()
        raise Exception(f"An error occurred while removing the project: {str(e)}")
