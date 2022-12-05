from itertools import chain
import json


def generate_diff(first_path, second_path):
    file1 = json.load(open(first_path))
    file2 = json.load(open(second_path))
    common_keys = set(file1) & set(file2)
    only_first_keys = set(file1) - set(file2)
    only_second_keys = set(file2) - set(file1)
    all_keys = set(file1.items()) | set(file2.items())

    def inner_():
        lines = []
        indent = '    '
        indent_neg = '  - '
        indent_pos = '  + '

        for elem in sorted(all_keys):
            key, value = elem
            if isinstance(value, bool):
                value = str(value).lower()
            if key in common_keys:
                if file1.get(key) == file2.get(key):
                    line = f'{indent}{key}: {value}'
                    lines.append(line)
                else:
                    line1 = f'{indent_neg}{key}: {file1.get(key)}'
                    line2 = f'{indent_pos}{key}: {file2.get(key)}'
                    lines.append(line1)
                    lines.append(line2)
                    common_keys.discard(key)
            elif key in only_first_keys:
                line = line = f'{indent_neg}{key}: {value}'
                lines.append(line)
            elif key in only_second_keys:
                line = line = f'{indent_pos}{key}: {value}'
                lines.append(line)
        result = chain('{', lines, '}')
        return '\n'.join(result)
    return inner_()
