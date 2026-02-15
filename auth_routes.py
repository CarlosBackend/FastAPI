from fastapi import APIRouter # Cria um roteador para criar as rotas
from models import Usuario, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
        Essa rota é uma rota de autenticação de usuarios.
    """
    return {"menssagem": "Você acessou a rota de autenticação","autenticado": False}

@auth_router.post("/criar_usuario")
async def criar_conta(email: str,senha: str, nome: str):
    Session = sessionmaker(bind=db)
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return {"menssagem": "Usuario ja cadastrado"}
    usuario = Usuario(nome,email,senha,True,False)
    session.add(usuario)
    session.commit()
    session.close()
    return {"menssagem": "Usuario criado com sucesso"}
