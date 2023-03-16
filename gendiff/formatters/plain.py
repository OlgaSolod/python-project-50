def change_value(value):
    if isinstance(value, (bool, int)):
        return str(value).lower()
    elif isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'
    else:
        return f'\'{value}\''


def make_plain(value):  # noqa: C901
    def iter_(keys, path):
        lines = []
        for key, val in keys.items():
            if isinstance(val, tuple):
                if val[0] == 'added':
                    lines.append(
                        f'Property \'{path + key}\' was added '
                        f'with value: {change_value(val[1])}'
                    )
                elif val[0] == 'removed':
                    lines.append(
                        f'Property \'{path + key}\' was removed'
                    )
                elif val[0] == 'changed':
                    lines.append(
                        f'Property \'{path + key}\' was updated. '
                        f'From {change_value(val[1])} to {change_value(val[2])}'
                    )
            else:
                lines.append(iter_(val, path + key + '.'))
        return '\n'.join(lines)
    return iter_(value, '')
