from pydantic import BaseModel

class Cliente(BaseModel):
    id_Cliente: int = None
    nome: str
    cpf: str
    compra_fiado: float
    dia_fiado: str
    senha: str