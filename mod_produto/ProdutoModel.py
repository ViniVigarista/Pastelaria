import db
from mod_produto.ProdutoModel import ProdutoDB

from sqlalchemy import Column, VARCHAR, CHAR, Integer
# ORM

class ProdutoDB(db.Base):
    _tablename_ = 'tb_produto'
    
    id_cliente = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(CHAR(11), unique=True, nullable=False)
    foto = Column(CHAR(11), nullable=False)
    valor_unitario = Column(float, nullable=False)

    def _init_(self, id_produto, nome, descricao, foto, valor_unitario):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.foto = foto
        self.valor_unitario = valor_unitario