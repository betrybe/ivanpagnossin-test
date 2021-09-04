from abc import ABC, abstractclassmethod
from typing import List

from inventory_report.models.product import ProductDict


class Importer(ABC):
    """Interface for inventory importers."""

    @abstractclassmethod
    def import_data(cls, filepath: str) -> List[ProductDict]:
        """Creates a list of products from an inventory file.

        Parameters:
        - filepath: path to the inventory file.

        Returns:
        List of products.
        """
