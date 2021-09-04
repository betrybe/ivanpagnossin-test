from datetime import date
from typing import Dict

from pydantic import BaseModel


ProductDict = Dict[str, str]


class CanonicalDate(date):
    """A date with convenient string representation."""

    def __repr__(self):
        return self.strftime('%Y-%m-%d')


class Product(BaseModel):
    """A single product in inventory."""

    id: str
    nome_do_produto: str
    nome_da_empresa: str
    data_de_fabricacao: CanonicalDate
    data_de_validade: CanonicalDate
    numero_de_serie: str
    instrucoes_de_armazenamento: str

    def as_dict(self) -> ProductDict:
        """Dict representation of a Product with dates as strings"""

        product = dict(self)

        for date_field in ['data_de_fabricacao', 'data_de_validade']:
            product[date_field] = str(product[date_field])

        return product
