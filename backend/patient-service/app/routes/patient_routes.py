from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.patient_model import Patient
from app.schemas.patient_schema import Patient as PatientSchema

router = APIRouter()


# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def home():
    return {"message": "Patient Service Running"}


@router.get("/patients")
def get_patients(db: Session = Depends(get_db)):

    patients = db.query(Patient).all()

    return patients


@router.get("/patients/{patient_id}")
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )

    if patient:
        return patient

    return {"message": "Patient not found"}


@router.post("/patients")
def create_patient(
    patient: PatientSchema,
    db: Session = Depends(get_db)
):

    new_patient = Patient(
        id=patient.id,
        name=patient.name,
        age=patient.age,
        disease=patient.disease
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return {
        "message": "Patient added successfully",
        "patient": new_patient
    }


@router.put("/patients/{patient_id}")
def update_patient(
    patient_id: int,
    updated_patient: PatientSchema,
    db: Session = Depends(get_db)
):

    patient = (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )

    if not patient:
        return {"message": "Patient not found"}

    patient.name = updated_patient.name
    patient.age = updated_patient.age
    patient.disease = updated_patient.disease

    db.commit()
    db.refresh(patient)

    return {
        "message": "Patient updated successfully",
        "patient": patient
    }


@router.delete("/patients/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )

    if not patient:
        return {"message": "Patient not found"}

    db.delete(patient)
    db.commit()

    return {
        "message": "Patient deleted successfully"
    }