from gendiff.parser import parse_data
import json

def generate_diff(path1, path2):
    dict1, dict2 = parse_data(path1, path2)
    def iter_(dict1, dict2, lines={}):
        # lines = {}
        for key in dict1:
            if key in dict2:
                if isinstance(dict1.get(key), dict) and isinstance(dict2.get(key), dict):
                    lines[key] = f'{iter_(dict1.get(key), dict2.get(key))}'
                if dict1.get(key) == dict2.get(key):
                    lines['unchanged'] = f' {key}: {dict2.get(key)}'
                else:
                    lines['changed'] = [
                        f'- {key}: {dict1.get(key)}',
                        f'+ {key}: {dict2.get(key)}'
                    ]
            elif key not in dict2:
                lines['removed']= f'- {key}: {dict1.get(key)}'
        for key in dict2:
            if key not in dict1:
                lines['added'] = f'+ {key}: {dict2.get(key)}'
        return lines
    return iter_(dict1, dict2)


print(json.dumps(generate_diff('tests/fixtures/nested3.json', 'tests/fixtures/nested4.json')))
