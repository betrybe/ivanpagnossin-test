from inventory_report.helpers.ordered_counter import OrderedCounter
from inventory_report.models.product import Product

from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products: list) -> str:
        """Generates report in string format.

        Parameters:
        products (list): List of products, each product a dictionary
        conforming inventory_report.models.product.Product

        Returns:
        str: Complete report
        """

        if not products:
            return cls.__empty_report()

        _products = [Product(**p) for p in products]

        inventory_by_company = \
            OrderedCounter([p.nome_da_empresa for p in _products]) \
            .items()

        TEMPLATE = '- {company}: {inventory}'
        complete_report = super().generate(products)
        complete_report += '\nProdutos estocados por empresa: \n'
        complete_report += '\n'.join([
            TEMPLATE.format(company=company, inventory=inventory)
            for (company, inventory) in inventory_by_company
        ])
        complete_report += '\n'

        return complete_report

    @classmethod
    def __empty_report(cls):
        return ''
