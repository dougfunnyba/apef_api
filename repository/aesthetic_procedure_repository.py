from model import Session
from schema import view_aesthetic_procedure, view_aesthetic_procedures

class AestheticProcedureRepository():
    
    def save(self, aesthetic_procedure):
        # criando conexão com a base
        session = Session()
        # adicionando um procedimentos estéticos
        session.add(aesthetic_procedure)
        # consolidando a inserção do novo procedimentos estéticos na tabela
        session.commit()
        return view_aesthetic_procedure(aesthetic_procedure), 200
    
    def get_aesthetic_procedures(self, aesthetic_procedure):
        # criando conexão com a base
        session = Session()
        # faz uma busca no banco de dados , retornando todos os procedimentos estéticos cadastrados
        aesthetic_procedures = session.query(aesthetic_procedure).all()

        if not aesthetic_procedures:
            # retorna uma lista vazia de procedimentos estéticos, caso a consulta não retorne nada 
            return {"procedimentos": []}, 200
        else:
            # retorna a representação dos procedimentos estéticos cadastrados
            return view_aesthetic_procedures(aesthetic_procedures), 200