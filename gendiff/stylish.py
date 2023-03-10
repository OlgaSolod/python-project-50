from itertools import chain


def formatter(value, space_counts=' ', counter=4):
    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return change_value(current_value)
        lines = []
        indent_size = depth + counter
        actual_indent = space_counts * (indent_size-2)
        previous_indent = space_counts * depth
        for key, val in current_value.items():
            if isinstance(val, tuple):
                if val[0] == 'added':
                    lines.append(f'{actual_indent}+ {key}: {iter_(val[1], indent_size)}')
                elif val[0] == 'removed':
                    lines.append(f'{actual_indent}- {key}: {iter_(val[1], indent_size)}')
                elif val[0] == 'changed':
                    lines.append(f'{actual_indent}- {key}: {iter_(val[1], indent_size)}')
                    lines.append(f'{actual_indent}+ {key}: {iter_(val[2], indent_size)}')
                elif val[0] == 'unchanged':
                    lines.append(f'{actual_indent}  {key}: {iter_(val[1], indent_size)}')
            else:
                lines.append(f'{actual_indent}  {key}: {iter_(val, indent_size)}')
        result = chain('{', lines, [previous_indent +'}'])
        return '\n'.join(result)
    return iter_(value, 0)

def change_value(value):
    if isinstance(value, str):
        return value
    if isinstance(value, (bool, int)):
        return str(value).lower()
    elif value == None:
        return 'null'
