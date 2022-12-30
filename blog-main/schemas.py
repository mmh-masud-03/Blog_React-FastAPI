from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title:str
    body: str 


class Blog(BlogBase):
    class Confg():
        orm_mode=True



class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]=[]
    class Confg():
        orm_mode=True
    


class ShowBLog(BaseModel):
    title: str
    body:str
    creator: ShowUser
    class Confg():
        orm_mode=True
