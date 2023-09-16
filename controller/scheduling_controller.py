from flask_openapi3 import Tag
from sqlalchemy.exc import IntegrityError

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
        """Adiciona um novo agendamento à base de dados

            Retorna uma representação do agendamento inserido.
        """
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

        # except IntegrityError as e:
        #     # retorna uma menssagem de IntegrityError caso o médico já esteja
        #     # cadastrado na base de dados
        #     error_msg = "O médico {} já esta cadastrado na dase de dados.".format(__scheduling_repository.name)
        #     return {"mesage": error_msg}, 409

        except Exception as e:
            # retorna uma menssagem para erros genéricos
            error_msg = "Não foi possível realizar o agendamento do paciente {}, motivo: {}.".format(scheduling.patient_name, e)
            return {"mesage": error_msg}, 400
        
    def get_schedulings(self):
        """Faz a busca por todos os médicos cadastrados

        Retorna uma representação da listagem dos médicos.
        """
        # chamando o repository para buscar os médicos cadastrados no banco de dados
        return self.__scheduling_repository.get_schedulings(Scheduling)