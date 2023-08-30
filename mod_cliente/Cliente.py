from pydantic import BaseModel

class CLiente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    compra_fiado: int
    dia_fiado: int
    senha: str = None