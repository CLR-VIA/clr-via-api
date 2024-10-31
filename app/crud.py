from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from hashlib import sha256
from uuid import UUID
from . import models, schemas


def get_user_by_id(db: Session, user_id: UUID) -> models.User:
    try:
        return db.query(models.User).filter(models.User.id == user_id).first()
    except Exception as e:
        raise Exception(f"An error occurred while retrieving users: {str(e)}")


def get_user_by_email(db: Session, email: str) -> models.User:
    try:
        return db.query(models.User).filter(models.User.email == email).first()
    except Exception as e:
        raise Exception(f"An error occurred while retrieving users: {str(e)}")


def get_users(db: Session, skip: int = 0, limit: int = None) -> list[models.User]:
    try:
        return db.query(models.User).offset(skip).limit(limit).all()
    except Exception as e:
        raise Exception(f"An error occurred while retrieving users: {str(e)}")


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
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

def update_user(db: Session, user_id: str, user: schemas.UserCreate) -> models.User:
    # Prepare the update data
    update_data = {}
    if user.password:
        update_data['hashed_password'] = sha256(user.password.encode()).hexdigest()
    if user.first_name:
        update_data['first_name'] = user.first_name
    if user.middle_name is not None:
        update_data['middle_name'] = user.middle_name
    if user.last_name:
        update_data['last_name'] = user.last_name
    if user.phone_number is not None:
        update_data['phone_number'] = user.phone_number
    if user.linkedin is not None:
        update_data['linkedin'] = user.linkedin
    if user.github is not None:
        update_data['github'] = user.github
    if user.portfolio is not None:
        update_data['portfolio'] = user.portfolio
    if user.summary is not None:
        update_data['summary'] = user.summary
    if user.skills:
        update_data['skills'] = user.skills
    if user.certifications:
        update_data['certifications'] = user.certifications

    try:
        # Execute the update, matching by user_id (UUID)
        result = db.query(models.User).filter(models.User.id == user_id).update(update_data)
        db.commit()

        # Check if any row was updated
        if result == 0:
            raise ValueError("User does not exist.")

        # Fetch and return the updated user
        db_user = db.query(models.User).filter(models.User.id == user_id).first()
        return db_user
    except IntegrityError:
        db.rollback()
        raise ValueError("A user with this email already exists.")
    except Exception as e:
        db.rollback()
        raise Exception(f"An error occurred while updating the user: {str(e)}")

def delete_user(db: Session, user_id: UUID) -> None:
    user = get_user_by_id(db, user_id)

    try:
        if user:
            db.delete(user)
            db.commit()
    except Exception as e:
        db.rollback()
        raise Exception(f"An error occurred while removing the project: {str(e)}")


def get_project_by_id(db: Session, project_id: UUID) -> models.Project:
    try:
        return db.query(models.Project).filter(models.Project.id == project_id).first()
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
