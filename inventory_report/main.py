#!/usr/bin/env python
"""Prints inventory report

Parameters:
1) Filepath to inventory (suported formats: .csv, .json and .xml)
2) Report type: "simples" or "completo"

Examples:
$ inventory_report data/inventory.json completo
$ python main.py data/inventory.xml simples
"""
import sys

from inventory_report.helpers.infer_report_task import infer_report_task
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        print('Verifique os argumentos', file=sys.stderr)
        return

    filepath = sys.argv[1]
    report_type = sys.argv[2]

    importer, report = infer_report_task(filepath, report_type)

    products = InventoryRefactor(importer).import_data(filepath, None)
    print(report.generate(products), end='')


if __name__ == '__main__':
    main()
