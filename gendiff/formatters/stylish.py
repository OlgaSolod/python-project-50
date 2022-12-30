from itertools import chain


def plain_format(diff):

    def inner_(dicti, depth):
        indent = '    '
        indent_neg = '  - '
        indent_pos = '  + '
        lines = []
        print(dicti)

    return inner_(diff)




def change_value(value):
    if isinstance(value, bool):
        value = str(value).lower()
    elif isinstance(value, None):
        value = ''
    return value


def create_line(indent, key, value):
    value = change_value(value)
    return f'{indent}{key}: {value}'