from collections import Counter
from datetime import date

from inventory_report.models.product import Product


class SimpleReport:
    @classmethod
    def generate(cls, products: list) -> str:
        """Generates report in string format.

        Parameters:
        products (list): List of products, each product a dictionary
        conforming inventory_report.models.product.Product

        Returns:
        str: Report
        """

        if not products:
            return cls.__pretty_print_report()

        _products = [Product(**p) for p in products]

        oldest_manufacturing_date = \
            sorted(
                _products,
                key=lambda product: product.data_de_fabricacao,
                reverse=True
            ) \
            .pop() \
            .data_de_fabricacao

        # TODO: empty list after filter
        today = date.today()
        closest_due_date = \
            sorted(
                [p for p in _products if p.data_de_validade >= today],
                key=lambda product: product.data_de_validade,
                reverse=True
            ) \
            .pop() \
            .data_de_validade

        # TODO: deal with draws
        most_common_company = \
            Counter([p.nome_da_empresa for p in _products]) \
            .most_common(1) \
            .pop()[0]

        return cls.__pretty_print_report(oldest_manufacturing_date,
                                         closest_due_date, most_common_company)

    @classmethod
    def __pretty_print_report(cls, oldest_manufacturing_date='?',
                              closest_due_date='?', most_common_company='?'):

        return (
            f'Data de fabricação mais antiga: {oldest_manufacturing_date}\n'
            f'Data de validade mais próxima: {closest_due_date}\n'
            'Empresa com maior quantidade de produtos '
            f'estocados: {most_common_company}\n'
        )
