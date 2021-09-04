from pathlib import Path
from typing import Dict, Tuple

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.importer import Importer
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.report import Report
from inventory_report.reports.simple_report import SimpleReport

from .validators import check_unsupported_file


def infer_report_task(filepath: str, report_type: str) -> Tuple[Importer,
                                                                Report]:
    IMPORTERS: Dict[str, Importer] = {
        '.csv': CsvImporter,
        '.json': JsonImporter,
        '.xml': XmlImporter
    }

    REPORTS: Dict[str, Report] = {
        'simples': SimpleReport,
        'completo': CompleteReport
    }

    if report_type not in REPORTS.keys():
        raise ValueError(f'"{report_type}" é um tipo de relatório '
                         'desconhecido. Use "simples" ou "completo".')

    suffix = Path(filepath).suffix
    check_unsupported_file(filepath, IMPORTERS.keys())

    return IMPORTERS[suffix], REPORTS[report_type]
