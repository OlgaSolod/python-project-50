import json


def generate_diff(path1, path2):
    dict1 = json.load(open(path1))
    dict2 = json.load(open(path2))
    general_set = set(dict1) | set(dict2)
    new_list = []
    for key in sorted(general_set):
        if key in dict1:
            if key in dict2:
                if dict2.get(key) == dict1.get(key):
                    val = change_bool(dict1.get(key))
                    string = f'    {key}: {val}'
                    new_list.append(string)
                else:
                    val1 = change_bool(dict1.get(key))
                    val2 = change_bool(dict2.get(key))
                    string1 = f'    {key}: {val1}'
                    string2 = f'  + {key}: {val2}'
                    new_list.append(string1)
                    new_list.append(string2)
            else:
                val = change_bool(dict1.get(key))
                string = f'  - {key}: {val}'
                new_list.append(string)
        else:
            val = change_bool(dict2.get(key))
            string = f'  + {key}: {val}' 
            new_list.append(string)
    result = '{\n' + '\n'.join(new_list) + '\n}'
    return result


def change_bool(value):
    if isinstance(value, bool):
        return str(value).lower()
    else:
        return value
