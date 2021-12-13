from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
db = SessionLocal()


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    value = Column(Integer)

Base.metadata.create_all(bind=engine)

item = Item(name="Item10", value=10000)
print(item.name)
print(item.value)
print(str(item.id))
db.add(item)
db.commit()
db.refresh(item)
print(item.name)
print(item.value)
print(str(item.id))

for row in db.query(Item).all():
    print(row.__dict__)

item_db = db.query(Item).filter_by(id=item.id)
print("XDDDDDDDDDDDDDDDDDDD", item.id,)
item_db.delete()
db.commit()
print("__________________________")
for row in db.query(Item).all():
    print(row.__dict__)