import json
from typing import List

from inventory_report.helpers.validators import check_unsupported_file
from inventory_report.importer.importer import Importer
from inventory_report.models.product import ProductDict


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filepath: str) -> List[ProductDict]:
        check_unsupported_file(filepath, ['.json'])

        # TODO: validate JSON format parsing entries with Product
        with open(filepath, 'r') as json_file:
            products = json.load(json_file)

        return products
