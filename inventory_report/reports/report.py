from abc import ABC, abstractclassmethod
from typing import List

from inventory_report.models.product import Product


class Report(ABC):
    @abstractclassmethod
    def generate(cls, products: List[Product]) -> str:
        """Generates report in string format.

        Parameters:
        - products: List of products.

        Returns:
        str: A string representation of the inventory report.
        """
