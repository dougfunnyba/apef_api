from flask_openapi3 import OpenAPI
from flask import redirect
from flask_cors import CORS
# from urllib.parse import unquote
# from unidecode import unidecode

from schema import DoctorViewSchema, DoctorSchema, ListDoctorsSchema
from schema import AestheticProcedureViewSchema, AestheticProceduresSchema, ListAestheticProcedureSchema
from schema import SchedulingSchema, SchedulingViewSchema, ListSchedulingSchema, SchedulingDelSchema 
from schema import SchedulingSearchByIdSchema, SchedulingSearchByDateSchema
from schema import ErrorSchema

# Import dos controllers usados pela Api
from controller.home_controller import HomeController
from controller.doctor_controller import DoctorController
from controller.aesthetic_procedure_controller import AestheticProceduresController
from controller.scheduling_controller import SchedulingController

# Instanciando os controllers usados pela API
home_controller = HomeController()
doctor_controller = DoctorController()
aesthetic_procedure_controller = AestheticProceduresController()
scheduling_controller = SchedulingController()

app = OpenAPI(__name__, info=home_controller.info)
CORS(app)

# Endpoint de redirecionamento para página principal da API
@app.get('/', tags=[home_controller.home_tag])
def home():
    """ Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    page = home_controller.home()
    return redirect(page)

# Endpoint para cadastro de médico
@app.post('/doctor', tags=[doctor_controller.doctor_tag],
          responses={"200": DoctorViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_doctor(form: DoctorSchema):
    """Adiciona um novo médico à base de dados

    Retorna uma representação do médico inserido.
    """
    return doctor_controller.add_doctor(form)

# Endpoint para listar os médicos cadastrados
@app.get('/doctors', tags=[doctor_controller.doctor_tag],
          responses={"200": ListDoctorsSchema, "404": ErrorSchema})
def get_doctors():
    """Faz a busca por todos os médicos cadastrados

    Retorna uma representação da listagem dos médicos.
    """
    return doctor_controller.get_doctors()

# Endpoint para cadastrar um procedimento estético
@app.post('/aesthetic_procedure', tags=[aesthetic_procedure_controller.aesthetic_procedure_tag],
          responses={"200": AestheticProcedureViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_aesthetic_procedure(form: AestheticProceduresSchema):
    """Adiciona um novo procedimento Estético à base de dados

    Retorna uma representação do procedimento Estético inserido.
    """
    return aesthetic_procedure_controller.add_aesthetic_procedure(form)

# Endpoint para listar os procedimentos estéticos cadastrados
@app.get('/aesthetic_procedures', tags=[aesthetic_procedure_controller.aesthetic_procedure_tag],
          responses={"200": ListAestheticProcedureSchema, "404": ErrorSchema})
def get_aesthetic_procedures():
    """Faz a busca por todos os procedimentos estéticos cadastrados

    Retorna uma representação da listagem dos procedimentos estéticos.
    """
    return aesthetic_procedure_controller.get_aesthetic_procedures()

# Endpoint para cadastrar um agendamento
@app.post('/scheduling', tags=[scheduling_controller.scheduling_tag],
          responses={"200": SchedulingViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_scheduling(form: SchedulingSchema):
    """Adiciona um novo agendamento à base de dados

    Retorna uma representação do agendamento inserido.
    """
    return scheduling_controller.add_scheduling(form)

# Endpoint para listar os agendamentos cadastrados
@app.get('/schedulings', tags=[scheduling_controller.scheduling_tag],
          responses={"200": ListSchedulingSchema, "404": ErrorSchema})
def get_schedulings():
    """Faz a busca por todos os agendamentos cadastrados

    Retorna uma representação da listagem dos agendamentos.
    """
    return scheduling_controller.get_schedulings()

# Endpoint para listar os agendamentos com base em uma determinada data
@app.get('/schedulings_by_date', tags=[scheduling_controller.scheduling_tag],
         responses={"200": ListSchedulingSchema, "404": ErrorSchema})
def get_schedulings_by_date(query: SchedulingSearchByDateSchema):
    """Faz a busca por agendamentos com base em uma data

    Retorna uma representação dos agendamentos.
    """
    return scheduling_controller.get_schedulings_by_date(query)

# Endpoint para deletar um agendamento cadastrado
@app.delete('/scheduling', tags=[scheduling_controller.scheduling_tag],
            responses={"200": SchedulingDelSchema, "404": ErrorSchema})
def del_produto(query: SchedulingSearchByIdSchema):
    """Deleta um agendamento a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    return scheduling_controller.del_scheduling(query)