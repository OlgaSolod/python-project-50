from itertools import chain
from gendiff.parsing import parsing


def generate_diff(filepath1, filepath2):
    file1 = parsing(filepath1)
    file2 = parsing(filepath2)
    all_keys = set(file1) | set(file2)
    difference = set(file1) - set(file2)
    added = set(file2) - set(file1)
    general = set(file1) & set(file2)
    indent = '    '
    indent_neg = '  - '
    indent_pos = '  + '

    lines = []
    for elem in sorted(all_keys):
        if elem not in difference and elem in general:
            if file1.get(elem) == file2.get(elem):
                line = create_line(indent, elem, file2.get(elem))
                lines.append(line)
            else:
                line1 = create_line(indent_neg, elem, file1.get(elem))
                line2 = create_line(indent_pos, elem, file2.get(elem))
                lines.append(line1)
                lines.append(line2)
        elif elem not in added:
            line = create_line(indent_neg, elem, file1.get(elem))
            lines.append(line)
        else:
            line = create_line(indent_pos, elem, file2.get(elem))
            lines.append(line)
    result = chain('{', lines, '}')
    return '\n'.join(result)


def transform_bool(value):
    if isinstance(value, bool):
        value = str(value).lower()
    return value


def create_line(indent, key, value):
    value = transform_bool(value)
    return f'{indent}{key}: {value}'
