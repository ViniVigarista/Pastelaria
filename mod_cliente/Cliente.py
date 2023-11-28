from pydantic import BaseModel

class Cliente(BaseModel):
    id_Cliente: int = None
    nome: str
    cpf: str
    senha: str
    resenha: str
    compra_fiado: float
    dia_fiado: str
    