from gendiff import generate_diff



path1 = 'tests/fixtures/file1.json'
path2 = 'tests/fixtures/file2.json'
print(path1)
result = open('tests/fixtures/expected.txt').read()



def test_plain():
    assert generate_diff(path1, path2) == result