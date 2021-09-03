import csv
from pathlib import Path

from inventory_report.importer.importer import Importer
from inventory_report.models.product import Product


class CsvImporter(Importer):
    def import_data(self, filepath):

        suffix = Path(filepath).suffix
        if suffix != '.csv':
            raise ValueError('Este importador não é capaz de lidar com '
                             f'arquivos {suffix}.')

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
