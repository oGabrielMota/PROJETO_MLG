from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///banco_dados.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()


class Conta(Base): 
    __tablename__ = "Conta"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome_conta = Column("nome_conta",String)
    meta = Column("meta",Integer)
    valor_vendido = Column("valor_vendido",Float)
    valor_restante = Column("valor_restante",Float)

    def __init__(self, nome_conta, meta, valor_vendido, valor_restante):
        self.nome_conta = nome_conta
        self.meta = meta
        self.valor_vendido = valor_vendido
        self.valor_restante = valor_restante



class Relatorio(Base): 
    __tablename__ = "Relatorio"

    id = Column("id", Integer, primary_key=True)
    data = Column("data",String)
    lucro_dia = Column("lucro_dia",Float)
    conta = Column("conta",ForeignKey("Conta.id"))

    def __init__(self, data, lucro_dia, conta):
        self.data = data
        self.lucro_dia = lucro_dia
        self.conta = conta


class Produtos(Base): 
    __tablename__ = "Produtos"

    sku = Column("SKU", String, primary_key=True)
    custo = Column("custo",Float)
    quantidade_estoque = Column("quantidade_estoque", Integer) #Opicional
    
    def __init__(self, sku, custo, quantidade_estoque):
        self.sku = sku
        self.custo = custo
        self.quantidade_estoque = quantidade_estoque


class Conteudo_Relatorio(Base): 
    __tablename__ = "Conteudo_Relatorio"

    id = Column("id", Integer, primary_key=True)
    mlb = Column("mlb", Integer)
    data= Column("data", String)
    unidade = Column("unidade",Integer)
    valor_venda = Column("valor_venda", Float)
    lucro_bruto = Column("lucro_bruto",Float)
    lucro_liquido = Column("lucro_liquido", Float, nullable=True)
    status = Column("status",String)
    sku = Column("sku",ForeignKey("Produtos.SKU"))

    def __init__(self, mlb, data, unidade, valor_venda, lucro_bruto , status,sku,lucro_liquido=None):
        self.mlb = mlb
        self.unidade = unidade
        self.data = data
        self.valor_venda = valor_venda
        self.lucro_bruto = lucro_bruto
        self.lucro_liquido = lucro_liquido
        self.status = status
        self.sku = sku





Base.metadata.create_all(bind=db)