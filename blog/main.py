from fastapi import FastAPI
from . import schemas, models, database
from .database import engine


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/blog")
def create(request: schemas.Blog):
    return request