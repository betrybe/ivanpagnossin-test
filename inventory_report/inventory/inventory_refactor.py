from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    """An iterable Inventory"""

    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def import_data(self, filepath: str, report_type: str) -> list:
        """Load inventory.

        Parameters:
        - filepath: path to the inventory file.
        - report_type: not used

        Returns:
        None
        """
        self.data += self.importer.import_data(filepath)
        return self.data

    def __iter__(self):
        return InventoryIterator(self.data)
