from fastapi import FastAPI
from app.routes.patient_routes import router
from app.database.db import engine, Base
from app.models.patient_model import Patient

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Patient Service API",
    version="1.0.0"
)

app.include_router(router)