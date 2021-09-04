from inventory_report.helpers.infer_report_task import infer_report_task


class Inventory():
    """Interface to interact with inventory files."""

    @classmethod
    def import_data(cls, filepath: str, report_type: str) -> str:
        """Prints an inventory report from inventory file.

        Parameters:
        - filepath: path to inventory file. Supported formats are .csv, .json
          and .xls.
        - report_type: "simples" or "completo".

        Returns:
        Report

        Exceptions:
        - ValueError: if the inventory file format is unsupported or if the
          desired report type is unknown.
        """
        importer, report = infer_report_task(filepath, report_type)
        products = importer.import_data(filepath)

        return report.generate(products)
