from fastapi import FastAPI
from routers import klass, student
import models

app = FastAPI()
app.include_router(klass.router, tags=['Classes'])
app.include_router(student.router, tags=['Students'])