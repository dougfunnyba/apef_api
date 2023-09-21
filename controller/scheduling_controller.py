from flask_openapi3 import Tag

from model import Scheduling
from repository.scheduling_repository import SchedulingRepository

class SchedulingController():

    def __init__(self):
        self.__scheduling_repository = SchedulingRepository()
        
    scheduling_tag = Tag(
            name="Scheduling", 
            description="Adição, visualização e remoção de agendamentos à base de dados"
        )
    
    def add_scheduling(self, form):
        scheduling = Scheduling(
            patient_name=form.patient_name,
            date_scheduling=form.date_scheduling,
            hour_scheduling=form.hour_scheduling,
            aesthetic_procedure_id=form.aesthetic_procedure_id,
            doctor_id=form.doctor_id
        )
        try:
            # chamando o repository para salvar o médico no banco de dados
            return self.__scheduling_repository.save(scheduling)

        except Exception as e:
            # retorna uma menssagem para erros genéricos
            error_msg = "Não foi possível realizar o agendamento do paciente {}, motivo: {}.".format(scheduling.patient_name, e)
            return {"mesage": error_msg}, 400
        
    def get_schedulings(self):
        # chamando o repository para buscar os agendamentos cadastrados no banco de dados
        return self.__scheduling_repository.get_schedulings(Scheduling)
    
    def get_schedulings_by_date(self, query):
        # chamando o repository para buscar os agendamentos 
        # com base em uma determinada data
        return self.__scheduling_repository.get_schedulings_by_date(Scheduling, query.date_scheduling)
    
    def del_scheduling(self, query):
        # chama o repository e deleta um agendamento do banco de dados
        return self.__scheduling_repository.delete(Scheduling, query.id)