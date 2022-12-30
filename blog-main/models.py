from sqlalchemy import Column, Integer, String
from database import Base

class Blog(Base):
    __tablename__='blog'

    id= Column(Integer, primary_key=True)
    title= Column(String)
    body= Column(String)

class User(Base):
    __tablename__='users'
    id= Column(Integer, primary_key=True)
    name= Column(String)
    email= Column(String)
    password= Column(String)