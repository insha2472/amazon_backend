from sqlalchemy import Column, Integer, String, Boolean
from db import Base
#user model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    address = Column(String)
    phone = Column(String)
    isprime = Column(Boolean)