from model import Session
from schema import view_scheduling, view_schedulings

class SchedulingRepository():
    
    def save(self, scheduling):
        # criando conexão com a base
        session = Session()
        # adicionando um agendamento
        session.add(scheduling)
        # consolidando a inserção do novo agendamento na tabela
        session.commit()
        return view_scheduling(scheduling), 200
    
    def get_schedulings(self, scheduling):
        # criando conexão com a base
        session = Session()
        # faz uma busca no banco de dados , retornando todos os agendamentos cadastrados
        schedulings = session.query(scheduling).all()

        if not schedulings:
            # retorna uma lista vazia de agendamentos, caso a consulta não retorne nada 
            return {"schedulings": []}, 200
        else:
            # retorna a representação dos agendamentos cadastrados
            return view_schedulings(schedulings), 200
        
    def get_schedulings_by_date(self, scheduling, date):
        # criando conexão com a base
        session = Session()
        # faz uma busca no banco de dados , retornando todos os agendamentos 
        # para uma determinada data
        schedulings = session.query(scheduling).filter(scheduling.date_scheduling == date).all()

        if not schedulings:
            # retorna uma lista vazia de agendamentos, caso a consulta não retorne nada 
            return {"schedulings": []}, 200
        else:
            # retorna a representação dos agendamentos para uma determinada data
            return view_schedulings(schedulings), 200
        
    def delete(self, scheduling, id):
        session = Session()
        # fazendo a remoção
        count = session.query(scheduling).filter(scheduling.id == id).delete()
        session.commit()

        if count:
            return {"mesage": "Agendamento deletado com sucesso."}
        else:
            error_msg = "Agendamento não encontrado na base de dados"
            return {"mesage": error_msg}, 404
