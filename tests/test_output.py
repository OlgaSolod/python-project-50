from gendiff.generate_diff import generate_diff
import pytest
import json

test_data_plain = [
    ("tests/fixtures/plain1.json",
     "tests/fixtures/plain2.json",
     "tests/fixtures/plain.txt"),
    ("tests/fixtures/plain1.yml",
     "tests/fixtures/plain2.yml",
     "tests/fixtures/plain.txt")
]

test_data_nested = [
    ("tests/fixtures/nested1.json",
     "tests/fixtures/nested2.json",
     "tests/fixtures/nested.txt"),
    ("tests/fixtures/nested1.yml",
     "tests/fixtures/nested2.yml",
     "tests/fixtures/nested.txt")
]

test_data_plain_ = [
    ("tests/fixtures/nested1.json",
     "tests/fixtures/nested2.json",
     "tests/fixtures/plain_.txt"),
    ("tests/fixtures/nested1.yml",
     "tests/fixtures/nested2.yml",
     "tests/fixtures/plain_.txt")
]

test_data_json = [
    ("tests/fixtures/nested1.json",
     "tests/fixtures/nested2.json",
     "tests/fixtures/json.txt"),
    ("tests/fixtures/nested1.yml",
     "tests/fixtures/nested2.yml",
     "tests/fixtures/json.txt")
]

@pytest.mark.parametrize('file_path1, file_path2, expected', test_data_plain)
def test_plain(file_path1, file_path2, expected):
    actual_result = generate_diff(file_path1, file_path2)
    with open(expected, 'r') as f:
        assert actual_result == f.read(), 'actual result is wrong'

@pytest.mark.parametrize('file_path1, file_path2, expected', test_data_nested)
def test_nested(file_path1, file_path2, expected):
    actual_result = generate_diff(file_path1, file_path2)
    with open(expected, 'r') as f:
        assert actual_result == f.read(), 'actual result is wrong'

@pytest.mark.parametrize('file_path1, file_path2, expected', test_data_plain_)
def test_plain_(file_path1, file_path2, expected):
    actual_result = generate_diff(file_path1, file_path2, 'plain')
    with open(expected, 'r') as f:
        assert actual_result == f.read(), 'actual result is wrong'

@pytest.mark.parametrize('file_path1, file_path2, expected', test_data_json)
def test_json(file_path1, file_path2, expected):
    actual_result = generate_diff(file_path1, file_path2, 'json')
    with open(expected, 'r') as f:
        assert actual_result == f.read(), 'actual result is wrong'