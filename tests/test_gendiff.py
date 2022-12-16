from gendiff import generate_diff



json1 = 'tests/fixtures/file1.json'
json2 = 'tests/fixtures/file2.json'


yml1 = 'tests/fixtures/file1.yml'
yml2 = 'tests/fixtures/file2.yml'

result = open('tests/fixtures/expected.txt').read()


def test_plain_json():
    assert generate_diff(json1, json2) == result

def test_plain_yml():
    assert generate_diff(yml1, yml2) == result


