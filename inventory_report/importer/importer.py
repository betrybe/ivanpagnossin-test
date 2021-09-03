from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(self, filepath: str) -> list:
        """Gera uma lista de produtos a partir de um arquivo de estoque.

        Parâmetros:
        - filepath (str): caminho para o arquivo de estoque.

        Retorna:
        list: Lista de produtos.
        """
