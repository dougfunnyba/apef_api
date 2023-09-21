
from flask_openapi3 import Tag
from sqlalchemy.exc import IntegrityError

from model import AestheticProcedures
from repository.aesthetic_procedure_repository import AestheticProcedureRepository

class AestheticProceduresController():

    def __init__(self):
        self.__aesthetic_procedure_repository = AestheticProcedureRepository()
        
    aesthetic_procedure_tag = Tag(
            name="Aesthetic Procedure", 
            description="Adição, visualização e remoção de procedimentos Estéticos à base de dados"
        )
    
    def add_aesthetic_procedure(self, form):
        aesthetic_procedure = AestheticProcedures(name=form.name, description=form.description)
        try:
            # chamando o repository para salvar o médico no banco de dados
            return self.__aesthetic_procedure_repository.save(aesthetic_procedure)

        except IntegrityError as e:
            # retorna uma menssagem de IntegrityError caso o médico já esteja
            # cadastrado na base de dados
            error_msg = "O Procedomento {} já esta cadastrado na dase de dados.".format(aesthetic_procedure.name)
            return {"mesage": error_msg}, 409

        except Exception as e:
            # retorna uma menssagem para erros genéricos
            error_msg = "Não foi possível cadastrar o procedimento {}, motivo: {}.".format(aesthetic_procedure.name, e)
            return {"mesage": error_msg}, 400
        
    def get_aesthetic_procedures(self):
        # chamando o repository para buscar os procedimentos estéticos cadastrados no banco de dados
        return self.__aesthetic_procedure_repository.get_aesthetic_procedures(AestheticProcedures)