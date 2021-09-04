import csv
from typing import List

from inventory_report.helpers.validators import check_unsupported_file
from inventory_report.importer.importer import Importer
from inventory_report.models.product import Product, ProductDict


class CsvImporter(Importer):
    """An inventory importer for inventory files in the CSV format."""

    @classmethod
    def import_data(cls, filepath: str) -> List[ProductDict]:
        check_unsupported_file(filepath, ['.csv'])

        with open(filepath, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            products = [
                Product(
                    id=id,
                    nome_do_produto=product,
                    nome_da_empresa=company,
                    data_de_fabricacao=manufacturing_date,
                    data_de_validade=due_date,
                    numero_de_serie=serial,
                    instrucoes_de_armazenamento=storage
                ).as_dict()
                for (id, product, company, manufacturing_date, due_date,
                     serial, storage) in reader
            ]

        return products
