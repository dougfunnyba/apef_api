from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os modelos
from model.base import Base
from model.doctor import Doctor
from model.aesthetic_procedures import AestheticProcedures
from model.scheduling import Scheduling

db_path = "database/"
# Verifica se o diretório não existe
if not os.path.exists(db_path):
   # Cria o diretório
   os.makedirs(db_path)

# URL de acesso ao sqlite local
db_url = 'sqlite:///%s/apef.sqlite3' % db_path

# Cria a engine de conexão com o banco
engine = create_engine(db_url, connect_args={"check_same_thread": False})

# Instancia um criador de sessão com o banco
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Verifica se o banco de dados já existe 
if not database_exists(engine.url):
    # Cria o banco de dados
    create_database(engine.url) 

# Cria as tabelas no banco de dados, caso não existam
Base.metadata.create_all(engine)