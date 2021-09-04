import json

from inventory_report.helpers.validators import check_unsupported_file
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(self, filepath):
        check_unsupported_file(filepath, '.json')

        # TODO: validate JSON format parsing entries with Product
        with open(filepath, 'r') as json_file:
            products = json.load(json_file)

        return products
