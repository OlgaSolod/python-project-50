from gendiff.parser import parse_data
from gendiff.stylish import formatter

def generate_diff(path1, path2):
    dict1, dict2 = parse_data(path1, path2)
    def iter_(dict1, dict2):
        diff = {}
        for key in sorted(set(dict1.keys()) | set(dict2.keys())):
            if key in dict1 and key not in dict2:
                diff[key] = ('removed', dict1[key])
            elif key in dict2 and key not in dict1:
                diff[key] = ('added', dict2[key])
            elif dict1[key] != dict2[key]:
                if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                    diff[key] = iter_(dict1[key], dict2[key])
                else:
                    diff[key] = ('changed', dict1[key], dict2[key])
            else:
                diff[key] = ('unchanged', dict1[key])
        return diff
    return iter_(dict1, dict2)


#print(formatter(generate_diff('tests/fixtures/nested1.json', 'tests/fixtures/nested2.json')))