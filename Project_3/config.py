from fastapi import FastAPI
from routers import students, classes, parents
import models

app = FastAPI()

app.include_router(parents.router, tags=['Parents'])
app.include_router(classes.router, tags=['Classes'])
app.include_router(students.router, tags=['Students'])