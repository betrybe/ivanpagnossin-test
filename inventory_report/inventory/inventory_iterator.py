from typing import List

from inventory_report.models.product import ProductDict


class InventoryIterator:
    def __init__(self, data: List[ProductDict]):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        try:
            datum = self.data[self.index]
        except IndexError:
            raise StopIteration()

        self.index += 1
        return datum
