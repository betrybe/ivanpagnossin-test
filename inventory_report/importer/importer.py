from abc import ABC, abstractclassmethod
from typing import List

from inventory_report.models.product import ProductDict


class Importer(ABC):
    @abstractclassmethod
    def import_data(cls, filepath: str) -> List[ProductDict]:
        """Gera uma lista de produtos a partir de um arquivo de estoque.

        Parâmetros:
        - filepath (str): caminho para o arquivo de estoque.

        Retorna:
        list: Lista de produtos.
        """
