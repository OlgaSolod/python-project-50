from gendiff import make_diff
from gendiff.parse import parsing


def generate_diff(filepath1, filepath2):
    file1 = parsing(filepath1)
    file2 = parsing(filepath2)
    diff = make_diff(file1, file2)
    print(diff)
    return diff
   

if __name__ == 'main':
    generate_diff()
   
generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
