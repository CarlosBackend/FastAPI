from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType


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

    def __init__(self, nome, email, senha, ativo, admin):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(base):
    __tablename__ = "pedidos"

    STATUS_PEDIDOS = (
        ("pendente", "Pendente"),
        ("cancelado", "Cancelado"),
        ("finalizado", "Finalizado"),
    )

    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    status = Column("status", ChoiceType(choices=STATUS_PEDIDOS), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), name="usuario_id", nullable=False)
    preco_total = Column("preco_total", Float, nullable=False)

    def __init__(self, usuario_id, status="pendente", preco_total=0.0):
        self.status = status
        self.usuario_id = usuario_id
        self.preco_total = preco_total
    

class ItemPedido(base):
    __tablename__ = "item_pedido"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    quantidade = Column("quantidade", Integer, nullable=False)
    sabor = Column("sabor", String, nullable=False)
    tamanho = Column("tamanho",String)
    preco = Column("preco", Float, nullable=False)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), name="pedido_id", nullable=False)

    def __init__(self, quantidade, sabor, tamanho, preco, pedido_id):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = preco
        self.pedido_id = pedido_id