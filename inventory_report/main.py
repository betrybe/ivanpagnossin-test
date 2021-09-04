import sys
from pathlib import Path

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def main():
    if len(sys.argv) < 3:
        print('Verifique os argumentos', file=sys.stderr)
        return

    filepath = sys.argv[1]
    report_type = sys.argv[2]

    IMPORTERS = {
        '.csv': CsvImporter,
        '.json': JsonImporter,
        '.xml': XmlImporter
    }

    REPORTS = {
        'simples': SimpleReport,
        'completo': CompleteReport
    }

    if report_type not in REPORTS.keys():
        raise ValueError(f'"{report_type}" é um tipo de relatório '
                         'desconhecido. Use "simples" ou "completo".')

    suffix = Path(filepath).suffix
    if suffix not in IMPORTERS.keys():
        raise ValueError(f'Formato de relatório inválido: {suffix}. '
                         'Use arquivos .csv, .json ou .xls')

    importer = IMPORTERS[suffix]()
    inventory = InventoryRefactor(importer)
    products = inventory.import_data(filepath)
    print(REPORTS[report_type].generate(products))


if __name__ == '__main__':
    main()
