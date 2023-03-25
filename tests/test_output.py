from gendiff.generate_diff import generate_diff
import pytest


test_data_simple = [
    ("tests/fixtures/simple1.json",
     "tests/fixtures/simple2.json",
     "tests/fixtures/simple_result.txt"),
    ("tests/fixtures/simple1.yml",
     "tests/fixtures/simple2.yml",
     "tests/fixtures/simple_result.txt")
]

test_data_nested = [
    ("tests/fixtures/nested1.json",
     "tests/fixtures/nested2.json",
     "tests/fixtures/nested_result.txt"),
    ("tests/fixtures/nested1.yml",
     "tests/fixtures/nested2.yml",
     "tests/fixtures/nested_result.txt")
]

test_data_plain = [
    ("tests/fixtures/nested1.json",
     "tests/fixtures/nested2.json",
     "tests/fixtures/plain_result.txt"),
    ("tests/fixtures/nested1.yml",
     "tests/fixtures/nested2.yml",
     "tests/fixtures/plain_result.txt")
]

test_data_json = [
    ("tests/fixtures/nested1.json",
     "tests/fixtures/nested2.json",
     "tests/fixtures/json_result.txt"),
    ("tests/fixtures/nested1.yml",
     "tests/fixtures/nested2.yml",
     "tests/fixtures/json_result.txt")
]


@pytest.mark.parametrize('file_path1, file_path2, expected', test_data_simple)
def test_plain(file_path1, file_path2, expected):
    actual_result = generate_diff(file_path1, file_path2)
    with open(expected, 'r') as f:
        assert f.read() == actual_result, 'Test simple is failed'


@pytest.mark.parametrize('file_path1, file_path2, expected', test_data_nested)
def test_nested(file_path1, file_path2, expected):
    actual_result = generate_diff(file_path1, file_path2)
    with open(expected, 'r') as f:
        assert f.read() == actual_result, 'Test nested is failed'


@pytest.mark.parametrize('file_path1, file_path2, expected', test_data_plain)
def test_plain_(file_path1, file_path2, expected):
    actual_result = generate_diff(file_path1, file_path2, 'plain')
    with open(expected, 'r') as f:
        assert f.read() == actual_result, 'Test plain is failed'


@pytest.mark.parametrize('file_path1, file_path2, expected', test_data_json)
def test_json(file_path1, file_path2, expected):
    actual_result = generate_diff(file_path1, file_path2, 'json')
    with open(expected, 'r') as f:
        assert f.read() == actual_result, 'Test json is failed'
