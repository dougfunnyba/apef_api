from pydantic import BaseModel
from typing import List

from model import Doctor

class DoctorSchema(BaseModel):
    """ Define a forma como um novo médico a ser inserido no banco de dados
        deve ser representado.
    """
    name: str = "Médico 1"

class DoctorViewSchema(BaseModel):
    """ Define como um médico será retornado.
    """
    id: int = 1
    name: str = "Médico 1"

class ListDoctorsSchema(BaseModel):
    """ Define como a lista de médicos será retornada.
    """
    doctors:List[DoctorViewSchema]

def view_doctor(doctor: Doctor):
    """ Retorna uma representação do médico.
    """
    return {
        "id": doctor.id,
        "name": doctor.name
    }

def view_doctors(doctors: List[Doctor]):
    """ Retorna uma representação dos médicos seguindo o schema definido em
        DoctorViewSchema.
    """
    result = []
    for doctor in doctors:
        result.append({
            "id": doctor.id,
            "name": doctor.name
        })

    return {"doctors": result}