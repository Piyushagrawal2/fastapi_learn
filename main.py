from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {'data': 'blog list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'This is an unpublished blog post.'}

@app.get("/blog")
def query(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'This is a blog list with limit {limit} and published status {published}'}
    else:
        return {'data': f'This is a blog list with limit {limit} and unpublished status.'}
    

@app.get("/blog/{id}")
def show(id: int):
    return {'data': f'This is blog post {id}.'}


@app.get('/blog/{id}/comments')
def comments(id: int, limit=10):
    return {'data': f'This is blog post {id} comments with limit {limit}.'}


class Blog(BaseModel):
    title: str
    body: str
    published: bool = True


@app.post('/blog')
def create_blog( request: Blog):
    return {'data': 'Blog created successfully', 'blog': request}