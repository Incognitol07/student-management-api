# app/main.py

from fastapi import FastAPI
from app.routers import student, auth
from app.database import engine, Base  # Assuming `engine` is your database engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student.router, prefix="/students", tags=["students"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}

