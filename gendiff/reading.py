from gendiff.parser import parse


def reading_files(file1, file2):
    if str(file1).endswith('json'):
        with open(file1) as f1:
            dict1 = parse(f1.read(), 'json')
        with open(file2) as f2:
            dict2 = parse(f2.read(), 'json')
    else:
        with open(file1) as f1:
            yaml_string = f1.read()
            dict1 = parse(yaml_string, 'yaml')
        with open(file2) as f2:
            yaml_string = f2.read()
            dict2 = parse(yaml_string, 'yaml')
    return dict1, dict2
