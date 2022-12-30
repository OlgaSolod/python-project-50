from gendiff import make_diff


json1 = 'tests/fixtures/file1.json'
json2 = 'tests/fixtures/file2.json'

nested_json1 =  'tests/fixtures/file1_nested.json'
nested_json2 = 'tests/fixtures/file2_nested.json'


yml1 = 'tests/fixtures/file1.yml'
yml2 = 'tests/fixtures/file2.yml'

nested_yml1 = 'tests/fixtures/file1_nested.yml'
nested_yml2 = 'tests/fixtures/file2_nested.yml'

result_plain = open('tests/fixtures/expected_plain.txt').read()
result_nested = open('tests/fixtures/expected_nested.txt').read()



def test_plain_json():
    assert make_diff(json1, json2) == result_plain


def test_plain_yml():
    assert make_diff(yml1, yml2) == result_plain

    
def test_nested_json():
    assert make_diff(nested_json1, nested_json2) == result_nested


def test_nested_yml():
    assert make_diff(nested_yml1, nested_yml2) == result_nested

