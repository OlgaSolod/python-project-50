from gendiff.parser import parse_data
import json
#from gendiff.stylish import formatter


def generate_diff(path1, path2):
    dict1, dict2 = parse_data(path1, path2)
    def iter_(dict1, dict2):
        diff = []
        for key in sorted(set(dict1.keys()) | set(dict2.keys())):
            if key in dict1 and key not in dict2:
                diff.append({'added': {key: dict1[key]}})
            elif key in dict2 and key not in dict1:
                diff.append({'removed': {key: dict2[key]}})
            elif dict1[key] != dict2[key]:
                if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                    diff.append(({key: iter_(dict1[key], dict2[key])}))
                else:
                    diff.append({'changed': {key: (dict1.get(key),dict2.get(key))}})
            else:
                diff.append({key: dict1[key]})
        return diff
    return iter_(dict1, dict2)

print(generate_diff('tests/fixtures/plain1.json', 'tests/fixtures/plain2.json'))

#formatter(generate_diff('tests/fixtures/nested1.json', 'tests/fixtures/nested2.json'))