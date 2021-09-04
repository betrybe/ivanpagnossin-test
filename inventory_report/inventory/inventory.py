from inventory_report.helpers.infer_report_task import infer_report_task


class Inventory():
    @classmethod
    def import_data(cls, filepath: str, report_type: str) -> str:
        """Prints an inventory report from inventory file

        Parameters:
        - filepath (str): path to inventory file. Supported formats are
                          .csv, .json and .xls
        - report_type (str): "simples" or "completo".

        Returns:
        str: Report
        """
        importer, report = infer_report_task(filepath, report_type)
        products = importer.import_data(filepath)

        return report.generate(products)
