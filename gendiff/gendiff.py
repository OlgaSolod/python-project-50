from itertools import chain
import json


def generate_diff(filepath1, filepath2):
    file1 = json.load(open(filepath1))
    file2 = json.load(open(filepath2))
    all_keys = set(file1) | set(file2)
    indent = '    '
    indent_neg = '  - '
    indent_pos = '  + '

    diff = get_diff(all_keys, file1, file2)
    lines = []
    for elem in diff:
        for key, value in elem.items():
            k, v = value
            v = transform_bool(v)
            if key == 'removed':
                line = create_line(indent_neg, k, v)

            elif key == 'added':
                line = create_line(indent_pos, k, v)

            elif key == 'unchanged':
                line = create_line(indent, k, v)
            elif key == 'changed -':
                line = create_line(indent_neg, k, v)
            else:
                line = create_line(indent_pos, k, v)

        lines.append(line)
    result = chain('{', lines, '}')
    return '\n'.join(result)


def get_diff(all_keys, file1, file2):
    diff = []
    for key in sorted(all_keys):
        if key not in file1:
            diff.append({'added': (key, file2.get(key))})
        elif key not in file2:
            diff.append({'removed': (key, file1.get(key))})
        elif file1.get(key) == file2.get(key):
            diff.append({'unchanged': (key, file1.get(key))})
        else:
            diff.append({'changed -': (key, file1.get(key))})
            diff.append({'changed +': (key, file2.get(key))})
    return diff


def transform_bool(value):
    if isinstance(value, bool):
        value = str(value).lower()
    return value


def create_line(indent, key, value):
    return f'{indent}{key}: {value}'
