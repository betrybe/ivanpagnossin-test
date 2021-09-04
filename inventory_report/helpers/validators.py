from pathlib import Path
from typing import List


def check_unsupported_file(filepath: str, suffixes: List[str]) -> None:
    """Check if file matches any of the expected suffixes.

    Parameters:
    - filepath: path to a file.
    - suffixes: list of expected suffixes (e.g., [".csv"]).

    Returns:
    None

    Exceptions:
    - ValueError: if file does not match any of the expected suffix.
    """

    suffix = Path(filepath).suffix
    if suffix not in suffixes:
        raise ValueError('Arquivo inválido ({suffix}).')
