class EmptyReportMixin:
    """Representation of an empty inventory report"""
    @classmethod
    def __empty_report(cls) -> str:
        return 'Estoque vazio.'
