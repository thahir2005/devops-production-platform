from datetime import datetime, timezone

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="Production Reliability API",
    description="A production-style application for DevOps deployment practice",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "service": "Production Reliability API",
        "status": "running",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/api/info")
def info():
    return {
        "application": "Production Reliability API",
        "environment": "development",
        "version": "1.0.0",
    }


Instrumentator().instrument(app).expose(app)