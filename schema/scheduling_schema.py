from pydantic import BaseModel
from typing import List

from model import Scheduling

class SchedulingSchema(BaseModel):
    """ Define a forma de como um novo agendamento a ser inserido
        no banco de dados deve ser representado
    """
    patient_name: str = "Paciente 1"
    date_scheduling: str = "01/02/2023"
    hour_scheduling: str = "08:00"
    aesthetic_procedure_id: int = 1
    doctor_id: int = 1

class SearchSchedulingByPatientNameSchema(BaseModel):
    """ Estrutura que representa uma busca pelo nome do paciente.
    """
    patient_name: str = "Paciente 1"

class SchedulingViewSchema(BaseModel):
    """ Define como um o agendamento será retornado.
    """
    id: int = 1
    patient_name: str = "Paciente 1"
    date_scheduling: str = "01/02/2023"
    hour_scheduling: str = "08:00"
    aesthetic_procedure_id: int = 1
    doctor_id: int = 1

class ListSchedulingSchema(BaseModel):
    """ Define como a lista agendamentos será retornado.
    """
    schedulings:List[SchedulingViewSchema]

class SchedulingDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str

class SchedulingSearchByIdSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do agendamento.
    """
    id: int = 1

class SchedulingSearchByDateSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base em uma data.
    """
    date_scheduling: str = "01/01/2023"

def view_scheduling(scheduling: Scheduling):
    """ Retorna uma representação de um agendamento.
    """
    return {
        "id": scheduling.id,
        "patient_name": scheduling.patient_name,
        "date_scheduling": scheduling.date_scheduling,
        "hour_scheduling": scheduling.hour_scheduling,
        "aesthetic_procedure": scheduling.aesthetic_procedure.name,
        "doctor": scheduling.doctor.name 
    }

def view_schedulings(schedulings: List[Scheduling]):
    """ Retorna uma representação dos agendamentos seguindo o schema definido em
        SchedulingViewSchema.
    """
    result = []
    for scheduling in schedulings:
        result.append({
            "id": scheduling.id,
            "patient_name": scheduling.patient_name,
            "date_scheduling": scheduling.date_scheduling,
            "hour_scheduling": scheduling.hour_scheduling,
            "aesthetic_procedure": scheduling.aesthetic_procedure.name,
            "doctor": scheduling.doctor.name
        })

    return {"schedulings": result}