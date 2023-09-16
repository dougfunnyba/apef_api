from flask_openapi3 import OpenAPI
from flask import redirect
from flask_cors import CORS
# from urllib.parse import unquote
# from unidecode import unidecode

from schema import DoctorViewSchema, DoctorSchema, ListDoctorsSchema
from schema import AestheticProcedureViewSchema, AestheticProceduresSchema, ListAestheticProcedureSchema
from schema import SchedulingSchema, SchedulingViewSchema, ListSchedulingSchema
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
    page = home_controller.home()
    return redirect(page)

# Endpoint para cadastro de médico
@app.post('/doctor', tags=[doctor_controller.doctor_tag],
          responses={"200": DoctorViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_doctor(form: DoctorSchema):
    return doctor_controller.add_doctor(form)

# Endpoint para listar os médicos cadastrados
@app.get('/doctors', tags=[doctor_controller.doctor_tag],
          responses={"200": ListDoctorsSchema, "404": ErrorSchema})
def get_doctors():
    return doctor_controller.get_doctors()

# Endpoint para cadastrar um procedimento estético
@app.post('/aesthetic_procedure', tags=[aesthetic_procedure_controller.aesthetic_procedure_tag],
          responses={"200": AestheticProcedureViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_aesthetic_procedure(form: AestheticProceduresSchema):
    return aesthetic_procedure_controller.add_aesthetic_procedure(form)

# Endpoint para listar os procedimentos estéticos cadastrados
@app.get('/aesthetic_procedures', tags=[aesthetic_procedure_controller.aesthetic_procedure_tag],
          responses={"200": ListAestheticProcedureSchema, "404": ErrorSchema})
def get_aesthetic_procedures():
    return aesthetic_procedure_controller.get_aesthetic_procedures()

# Endpoint para cadastrar um agendamento
@app.post('/scheduling', tags=[scheduling_controller.scheduling_tag],
          responses={"200": SchedulingViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_scheduling(form: SchedulingSchema):
    return scheduling_controller.add_scheduling(form)

# Endpoint para listar os agendamentos cadastrados
@app.get('/schedulings', tags=[scheduling_controller.scheduling_tag],
          responses={"200": ListSchedulingSchema, "404": ErrorSchema})
def get_schedulings():
    return scheduling_controller.get_schedulings()