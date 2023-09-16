from sqlalchemy import Column, String, Integer

from  model import Base

class AestheticProcedures(Base):
   __tablename__ = 'aesthetic_procedures' 

   id = Column(Integer, primary_key=True)
   name = Column(String(250), unique=True, nullable=False)
   description = Column(String(4000))

   def __init__(self, name:str, description:str):
        """
        Cria um procedimento estético  

        Arguments:
            name: Nome do procedimento.
            description: Descrição do procedimento.
        """
        self.name = name
        self.description = description