from tempfile import TemporaryDirectory


def get_temp_dir():
    dir = TemporaryDirectory()
    try:
        yield dir.name
    finally:
        del dir
