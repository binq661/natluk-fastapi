from user import schemas
from user.models import user
from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from database_utils.hashing import hash_password


def create(user: schemas.UserCreate, db: Session):
    user_db = db.query(models.User).filter(models.User.email == user.email).first()
    if user_db:
        raise HTTPException(status_code=409, detail="Email already registered.")
    user_data = user.dict()
    user_data["password"] = hash_password(user.password)
    new_user = models.User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def read(user_id: int, db: Session):
    user = db.query(models.User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user_id} not found",
        )
    return user


def read_all(db: Session):
    users = db.query(models.User).all()
    return users


def update(user_id: int, user: schemas.UserCreate, db: Session):
    user_from_db = db.query(models.User).filter_by(id=user_id).first()
    if not user_from_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )

    user_from_db.email = user.email
    user_from_db.password = hash_password(user.password)
    db.commit()


def delete(user_id: int, db: Session):
    user = db.query(models.User).filter_by(id=user_id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found"
        )
    user.delete()
    db.commit()
