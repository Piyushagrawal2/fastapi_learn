from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {'data': {'name': 'Piyush Agrawal', 'age': 21}}

@app.get("/about")
def about():
    return {'data': 'This is about page of FastAPI application.'}
