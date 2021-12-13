from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Path, Response
import schemas
import services
from database import get_db

users_router = APIRouter(prefix="/user", tags=["Users"])


@users_router.get("/all", response_model=list[schemas.UserOut], tags=["AllUsers"])
def read_all_users(db: Session = Depends(get_db)):
    return services.read_all(db)


@users_router.post("/", response_model=schemas.UserOut, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create(user, db)


@users_router.get("/{user_id}", response_model=schemas.UserOut, status_code=200)
def read_user(user_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    return services.read(user_id, db)


@users_router.put("/{user_id}", status_code=202)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    services.update(user_id, user, db)
    return "OK"


@users_router.delete("/{user_id}", status_code=204, response_class=Response)
def delete_user(user_id, db: Session = Depends(get_db)):
    services.delete(user_id, db)
