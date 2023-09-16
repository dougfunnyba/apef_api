from sqlalchemy import Column, String, Integer

from  model import Base

class Doctor(Base):
   __tablename__ = 'doctor' 

   id = Column(Integer, primary_key=True)
   name = Column(String(250), unique=True, nullable=False)

   def __init__(self, name:str):
        """
        Cria um médico

        Arguments:
            name: Nome do médico.
        """
        self.name = name