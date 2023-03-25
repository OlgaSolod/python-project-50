def to_string(value):
    if isinstance(value, (bool, int)):
        return str(value).lower()
    elif isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'
    else:
        return f'\'{value}\''


def format_plain(value):  # noqa: C901
    def iter_(keys, path):
        lines = []
        for key, val in keys.items():
            if isinstance(val, tuple):
                if val[0] == 'added':
                    lines.append(
                        f'Property \'{path + key}\' was added '
                        f'with value: {to_string(val[1])}'
                    )
                elif val[0] == 'removed':
                    lines.append(
                        f'Property \'{path + key}\' was removed'
                    )
                elif val[0] == 'changed':
                    lines.append(
                        f'Property \'{path + key}\' was updated. '
                        f'From {to_string(val[1])} to {to_string(val[2])}'
                    )
            else:
                lines.append(iter_(val, path + key + '.'))
        return '\n'.join(lines)
    return iter_(value, '')
