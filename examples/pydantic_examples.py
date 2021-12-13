from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional, Union


class Person(BaseModel):
    name: str
    surname: Optional[str]
    personal_email: EmailStr
    birth_date: date
    money: Union[int, float] # [float, int]
    kids_count: int = 0


instance = Person(money="1")
print(instance.money, type(instance.money))
print(instance.dict())
instance = Person(money="1", kids_count=0)
print(instance.dict(exclude_unset=True))

print(instance.dict(exclude_defaults=True))

