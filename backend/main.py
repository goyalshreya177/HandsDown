
from fastapi import FastAPI

app = FastAPI(
    title="HandsDown API",
    description="Backend for the HandsDown tactile sensing simulator",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to HandsDown API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "project": "HandsDown"
    }
