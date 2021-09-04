from pathlib import Path


def check_unsupported_file(filepath: str, expected_suffix: str) -> None:
    """Raises ValueError if filepath does not have the expected suffix.

    Parameters:
    - filepath (str): Path to a file.
    - expected_suffix (str): Expected suffix (e.g., ".csv").

    Returns:
    None
    """

    suffix = Path(filepath).suffix
    if suffix != expected_suffix:
        raise ValueError('Arquivo {suffix} não é suportado.')
