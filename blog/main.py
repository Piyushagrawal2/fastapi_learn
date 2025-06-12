from fastapi import FastAPI, Depends
from . import schemas, models, database
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog")
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    db.add(models.Blog(**request.dict()))
    db.commit()
    db.refresh()
    return request