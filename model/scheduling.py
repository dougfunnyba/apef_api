from sqlalchemy import Column, String, Integer, ForeignKey 
from sqlalchemy.orm import backref, relationship

from  model import Base, AestheticProcedures, Doctor

class Scheduling(Base):
    __tablename__ = 'scheduling'

    id = Column(Integer, primary_key=True)
    patient_name = Column(String(250), nullable=False)
    date_scheduling = Column(String(10), nullable=False)
    hour_scheduling = Column(String(5), nullable=False)

    # Relacionamento entre Agendamento e Procedimento.
    aesthetic_procedure_id = Column(Integer, ForeignKey("aesthetic_procedures.id"))
    aesthetic_procedure = relationship("AestheticProcedures", backref=backref("scheduling", uselist=False))

    # Relacionamento entre Médico e Agendamento.
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    doctor = relationship("Doctor", backref=backref("scheduling", uselist=False))

    def __init__(self, patient_name: str, date_scheduling: str, hour_scheduling: str, 
                 aesthetic_procedure_id: int, doctor_id: int):
        """
        Cria um agendamento

        Arguments:
            patient_name: Nome do Paciente.
            date_scheduling: Data do agendamento.
            hour_scheduling: Hora do agendamento.
            aesthetic_procedure_id: ID do procedimento.
            doctor_id: ID do médico
        """
        self.patient_name = patient_name
        self.date_scheduling = date_scheduling
        self.hour_scheduling = hour_scheduling
        self.aesthetic_procedure_id = aesthetic_procedure_id
        self.doctor_id = doctor_id
