from model import Session
from schema import view_scheduling, view_schedulings

class SchedulingRepository():
    
    def save(self, scheduling):
        # criando conexão com a base
        session = Session()
        # adicionando um médico
        session.add(scheduling)
        # consolidando a inserção do novo médico na tabela
        session.commit()
        return view_scheduling(scheduling), 200
    
    def get_schedulings(self, scheduling):
        # criando conexão com a base
        session = Session()
        # faz uma busca no banco de dados , retornando todos os médicos cadastrados
        schedulings = session.query(scheduling).all()

        if not schedulings:
            # retorna uma lista vazia de médicos, caso a consulta não retorne nada 
            return {"agendamentos": []}, 200
        else:
            # retorna a representação dos médicos cadastrados
            return view_schedulings(schedulings), 200