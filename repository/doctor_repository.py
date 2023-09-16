from model import Session
from schema import view_doctor, view_doctors

class DoctorRepository():
    
    def save(self, doctor):
        # criando conexão com a base
        session = Session()
        # adicionando um médico
        session.add(doctor)
        # consolidando a inserção do novo médico na tabela
        session.commit()
        return view_doctor(doctor), 200
    
    def get_doctors(self, doctor):
        # criando conexão com a base
        session = Session()
        # faz uma busca no banco de dados , retornando todos os médicos cadastrados
        doctors = session.query(doctor).all()

        if not doctors:
            # retorna uma lista vazia de médicos, caso a consulta não retorne nada 
            return {"medicos": []}, 200
        else:
            # retorna a representação dos médicos cadastrados
            return view_doctors(doctors), 200