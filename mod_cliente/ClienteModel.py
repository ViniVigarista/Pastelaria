import db
from mod_cliente.ClienteModel import ClienteDB
from sqlalchemy import Column, VARCHAR, CHAR, Integer
# ORM

class ClienteDB(db.Base):
    _tablename_ = 'tb_cliente'
    
    id_cliente = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    cpf = Column(CHAR(11), unique=True, nullable=False)
    telefone = Column(CHAR(11), nullable=False)
    compra_fiado = Column(float)
    dia_fiado = Column(Integer)
    senha = Column(VARCHAR(200), nullable=False)

    def _init_(self, id_cliente, nome, cpf, telefone, compra_fiado, dia_fiado, senha):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.compra_fiado = compra_fiado
        self.dia_fiado = dia_fiado
        self.senha = senha