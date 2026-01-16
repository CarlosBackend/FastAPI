from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
        Essa rota é uma rota de autenticação de usuarios.
    """
    return {"menssagem": "Você acessou a rota de autenticação","autenticado": False}