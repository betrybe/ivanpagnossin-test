from pathlib import Path

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory():
    @classmethod
    def import_data(cls, filepath: str, report_type: str) -> str:
        """Importa um relatório de um arquivo.

        Parâmetros:
        filepath (str): caminho para o arquivo de relatório.
            Formatos aceitos: .csv, .json e .xls
        report_type (str): tipo de relatório a gerar.
            Pode ser "simples" ou "completo".

        Retorna:
        str: Relatório
        """

        IMPORTERS = {
            '.csv': CsvImporter
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

        products = \
            IMPORTERS[suffix]() \
            .import_data(filepath)

        return REPORTS[report_type].generate(products)
