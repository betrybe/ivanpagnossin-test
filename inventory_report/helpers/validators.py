from pathlib import Path
from typing import List


def check_unsupported_file(filepath: str, suffixes: List[str]) -> None:
    """Raises ValueError if filepath does not have the expected suffix.

    Parameters:
    - filepath: Path to a file.
    - suffixes: List of expected suffixes (e.g., [".csv"]).

    Returns:
    None
    """

    suffix = Path(filepath).suffix
    if suffix not in suffixes:
        raise ValueError('Arquivo inválido ({suffix}).')
