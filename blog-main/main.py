from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas
from models import Blog

Base.metadata.create_all(engine)

app = FastAPI()
# create a db instance to talk to the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {"app_name": "blog app"}

#create blog
@app.post('/blog')
def create_blog(blog: schemas.Blog, db: Session= Depends(get_db)): 
    new_blog= models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()                                                              #creating new blog
    db.refresh(new_blog)
    return new_blog


#delete blog
@app.delete('/blog/{id}')
def destroy(id, db: Session= Depends(get_db)):
    blog=db.query(models.Blog).get(id)
    if not blog.first():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


#update blog
@app.put('/blog/{id}')
def update(id:int, request: schemas.Blog, db: Session= Depends(get_db)):
    blog=db.query(models.Blog).get(id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.update(request)
    db.commit()
    return 'updated'


#get all blogs
@app.get('/blog')
def all(db: Session= Depends(get_db)):
    blogs= db.query(models.Blog).all()
    return blogs


#get a particular blog
@app.get('/blog/{id}')
def show_blog_by_id(id: int, db: Session= Depends(get_db)):
    blog=db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} does not exists")
    return blog





#create user
@app.post('/user', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session= Depends(get_db)):
    new_user= models.User(name=request.name, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



#get user
@app.get('/user/{id}',response_model=schemas.ShowUser)
def get_user(id: int, db: Session= Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exists")
    return user
