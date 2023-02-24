import json


def generate_diff(path1, path2):
    dict1 = json.load(open(path1))
    dict2 = json.load(open(path2))
    general_set = set(dict1) | set(dict2)
    new_list = []
    for key in sorted(general_set):
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                val = change_bool(dict1.get(key))
                new_list.append(f'    {key}: {val}')
            else:
                val1 = change_bool(dict1.get(key))
                val2 = change_bool(dict2.get(key))
                new_list.extend([f'  - {key}: {val1}', f'  + {key}: {val2}'])
        elif key in dict1:
            val = change_bool(dict1.get(key))
            new_list.append(f'  - {key}: {val}')
        else:
            val = change_bool(dict2.get(key))
            new_list.append(f'  + {key}: {val}')
    result = '{\n' + '\n'.join(new_list) + '\n}'
    return result


def change_bool(value):
    if isinstance(value, bool):
        return str(value).lower()
    else:
        return value
