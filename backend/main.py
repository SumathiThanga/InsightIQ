
from fastapi import FastAPI

app = FastAPI(
    title="InsightIQ API",
    description="Intelligent Document Analytics Platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to InsightIQ API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "InsightIQ API",
    }
