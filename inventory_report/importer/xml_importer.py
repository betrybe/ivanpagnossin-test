import xml.etree.ElementTree as ET

from inventory_report.helpers.validators import check_unsupported_file
from inventory_report.importer.importer import Importer
from inventory_report.models.product import Product


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath: str) -> list:
        check_unsupported_file(filepath, ['.xml'])

        fields = Product.__fields__.keys()
        tree = ET.parse(filepath)
        products = [
            Product(**{f: product.find(f).text for f in fields}).as_dict()
            for product in tree.getroot()
        ]

        return products
