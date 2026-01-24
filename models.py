from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///banco.db")
base = declarative_base()

class Usuario(base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, nullable=False)
    admin = Column("admin", Boolean, nullable=False)