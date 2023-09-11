from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    compra_fiado: int
    dia_fiado: str
    senha: str