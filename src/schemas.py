from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    password: str
    is_active: bool = True

    class Config:
        orm_mode = True
