from fastapi import APIRouter
order_router = APIRouter(prefix="/pedidos", tags=["orders"])

@order_router.get("/")
async def pedidos():
    """
    Essa rota é uma rota de pedidos do sistema.
    """
    return {"mensagem": "Você acessou a rota de pedidos"}