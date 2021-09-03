from datetime import date

from pydantic import BaseModel


class Product(BaseModel):
    id: int
    nome_do_produto: str
    nome_da_empresa: str
    data_de_fabricacao: date
    data_de_validade: date
    numero_de_serie: str
