from fastapi import FastAPI
from app.routes.patient_routes import router

app = FastAPI(
    title="Patient Service API",
    version="1.0.0"
)

app.include_router(router)