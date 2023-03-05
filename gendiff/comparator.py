from gendiff.parser import parse_data


def generate_diff(path1, path2):
    dict1, dict2 = parse_data(path1, path2)
    general_set = set(dict1) | set(dict2)
    def iter_():
        lines = {}
        for key in sorted(general_set):
            if key in dict1 and key in dict2:

                if dict1[key] == dict2[key]:
                    print(1)
                    val = change_bool(dict1.get(key))
                    lines['unchanged'] = f'  {key}: {val}'
                    
                else:
                    val1 = change_bool(dict1.get(key))
                    val2 = change_bool(dict2.get(key))
                    lines['changed'] = [f'- {key}: {val1}' f'  + {key}: {val2}']

            elif key in dict1:
                val = change_bool(dict1.get(key))
                lines['deleted'] = f'- {key}: {val}'
            else:
                val = change_bool(dict2.get(key))
                lines['added'] = f'+ {key}: {val}'
        return lines
        # result = '{\n' + '\n'.join(lines) + '\n}'
        # return result


    # def change_bool(value):
    #     if isinstance(value, bool):
    #         return str(value).lower()
    #     else:
    #         return value

print(generate_diff('tests/fixtures/plain1.json', 'tests/fixtures/plain2.json'))