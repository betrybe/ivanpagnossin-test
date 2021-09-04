from abc import ABC, abstractclassmethod


class Importer(ABC):
    @abstractclassmethod
    def import_data(cls, filepath: str) -> list:
        """Gera uma lista de produtos a partir de um arquivo de estoque.

        Parâmetros:
        - filepath (str): caminho para o arquivo de estoque.

        Retorna:
        list: Lista de produtos.
        """
