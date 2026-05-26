from fastapi import APIRouter
from app.schemas.patient_schema import Patient

router = APIRouter()


patients = [
    {
        "id": 1,
        "name": "Rahul Sharma",
        "age": 29,
        "disease": "Fever"
    },
    {
        "id": 2,
        "name": "Priya Singh",
        "age": 35,
        "disease": "Diabetes"
    }
]


@router.get("/")
def home():
    return {"message": "Patient Service Running"}


@router.get("/patients")
def get_patients():
    return patients


@router.get("/patients/{patient_id}")
def get_patient(patient_id: int):

    for patient in patients:
        if patient["id"] == patient_id:
            return patient

    return {"message": "Patient not found"}


@router.post("/patients")
def create_patient(patient: Patient):

    patients.append(patient.dict())

    return {
        "message": "Patient added successfully",
        "patient": patient
    }