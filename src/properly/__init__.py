import os


def setup() -> None:
    """ Enable unbuffered, say. """
    os.environ['PYTHON_UNBUFFERED'] = "1"
