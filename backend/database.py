### A responsabilidade deste arquivo é de realizar a conexão com o banco de dados sempre que necessário

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"
engine = create_engine(url=POSTGRES_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db ### Este comando faz com que a função não seja terminada e seu resultado possa ser chamado diversas vezes
    finally:
        db.close()