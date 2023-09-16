from flask_openapi3 import Tag
from sqlalchemy.exc import IntegrityError

from model import Doctor
from repository.doctor_repository import DoctorRepository

class DoctorController():

    def __init__(self):
        self.__doctor_repository = DoctorRepository()
        
    doctor_tag = Tag(
            name="Doctor", 
            description="Adição, visualização e remoção de médicos à base de dados"
        )
    
    def add_doctor(self, form):
        """Adiciona um novo médico à base de dados

            Retorna uma representação do médico inserido.
        """
        doctor = Doctor(name=form.name)
        try:
            # chamando o repository para salvar o médico no banco de dados
            return self.__doctor_repository.save(doctor)

        except IntegrityError as e:
            # retorna uma menssagem de IntegrityError caso o médico já esteja
            # cadastrado na base de dados
            error_msg = "O médico {} já esta cadastrado na dase de dados.".format(doctor.name)
            return {"mesage": error_msg}, 409

        except Exception as e:
            # retorna uma menssagem para erros genéricos
            error_msg = "Não foi possível cadastrar o médico {}, motivo: {}.".format(doctor.name, e)
            return {"mesage": error_msg}, 400
        
    def get_doctors(self):
        """Faz a busca por todos os médicos cadastrados

        Retorna uma representação da listagem dos médicos.
        """
        # chamando o repository para buscar os médicos cadastrados no banco de dados
        return self.__doctor_repository.get_doctors(Doctor)