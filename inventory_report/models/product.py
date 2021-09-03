from datetime import date

from pydantic import BaseModel


class CanonicalDate(date):
    def __repr__(self):
        return self.strftime('%Y-%m-%d')


class Product(BaseModel):
    id: int
    nome_do_produto: str
    nome_da_empresa: str
    data_de_fabricacao: CanonicalDate
    data_de_validade: CanonicalDate
    numero_de_serie: str
    instrucoes_de_armazenamento: str

    def as_dict(self) -> dict:
        """Representação dict de um Product"""

        product = dict(self)

        for date_field in ['data_de_fabricacao', 'data_de_validade']:
            product[date_field] = str(product[date_field])

        return product
