from gendiff.comparator import generate_diff
import pytest

test_data = [
    ("tests/fixtures/json1.json",
     "tests/fixtures/json2.json",
     "tests/fixtures/result_1.txt"),
    ("tests/fixtures/json3.json",
     "tests/fixtures/json4.json",
     "tests/fixtures/result_2.txt"),
    ("tests/fixtures/yaml1.yml",
     "tests/fixtures/yaml2.yml",
     "tests/fixtures/result_1.txt")
]


@pytest.mark.parametrize('file_path1, file_path2, expected', test_data)
def test_plain(file_path1, file_path2, expected):
    actual_result = generate_diff(file_path1, file_path2)
    with open(expected, 'r') as f:
        assert actual_result == f.read(), 'actual result is wrong'
