from src.utils import read_file_operations


def test_read_file_operations():
    assert read_file_operations(filename="data/operations1.json") == []
