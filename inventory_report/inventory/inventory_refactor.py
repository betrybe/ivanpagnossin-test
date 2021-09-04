from typing import List

from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.models.product import ProductDict


class InventoryRefactor:
    """An iterable Inventory"""

    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def import_data(self, filepath: str,
                    report_type: str) -> List[ProductDict]:
        """Load inventory.

        Parameters:
        - filepath: path to the inventory file.
        - report_type: not used

        Returns:
        List of products in inventory.
        """
        self.data += self.importer.import_data(filepath)
        return self.data

    def __iter__(self):
        return InventoryIterator(self.data)
