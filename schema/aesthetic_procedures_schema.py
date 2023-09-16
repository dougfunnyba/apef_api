from pydantic import BaseModel
from typing import List

from model import AestheticProcedures


class AestheticProceduresSchema(BaseModel):
    """ Define a forma como um novo procedimento a ser inserido no 
        banco de dados deve ser representado.
    """
    name: str = "Procedimento base"
    description: str = ""

class AestheticProcedureViewSchema(BaseModel):
    """ Define como um procedimento estético será retornado.
    """
    id: int = 1
    name: str = "Procedimento base"
    description: str = ""

class ListAestheticProcedureSchema(BaseModel):
    """ Define como a lista de procedimentos estéticos será retornada.
    """
    aesthetic_procedures:List[AestheticProcedureViewSchema]

def view_aesthetic_procedure(aesthetic_procedure: AestheticProcedures):
    """ Retorna um procedimento estético.
    """
    return {
        "id": aesthetic_procedure.id,
        "name": aesthetic_procedure.name,
        "description": aesthetic_procedure.description
    }

def view_aesthetic_procedures(aesthetic_procedures: List[AestheticProcedures]):
    """ Retorna uma representação dos procedimentos estéticos seguindo o schema definido em
        AestheticProcedureViewSchema.
    """
    result = []
    for aesthetic_procedure in aesthetic_procedures:
        result.append({
            "id": aesthetic_procedure.id,
            "name": aesthetic_procedure.name,
            "description": aesthetic_procedure.description
        })

    return {"aesthetic_procedures": result}