from gendiff.parser import parse_data
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain


def generate_diff(path1, path2, format='stylish'):
    dict1, dict2 = parse_data(path1, path2)
    if format == 'stylish':
        return make_stylish(compare_dicts(dict1, dict2))
    elif format == 'plain':
        return make_plain(compare_dicts(dict1, dict2))


def compare_dicts(dict1, dict2):
    diff = {}
    for key in sorted(set(dict1.keys()) | set(dict2.keys())):
        if is_removed(key, dict1, dict2):
            diff[key] = ('removed', dict1[key])
        elif is_added(key, dict1, dict2):
            diff[key] = ('added', dict2[key])
        elif is_changed(key, dict1, dict2):
            if is_dict(dict1[key]) and is_dict(dict2[key]):
                diff[key] = compare_dicts(dict1[key], dict2[key])
            else:
                diff[key] = ('changed', dict1[key], dict2[key])
        else:
            diff[key] = ('unchanged', dict1[key])
    return diff


def is_dict(value):
    return isinstance(value, dict)


def is_added(key, dict1, dict2):
    return key in dict2 and key not in dict1


def is_removed(key, dict1, dict2):
    return key in dict1 and key not in dict2


def is_unchanged(key, dict1, dict2):
    return key in dict1 and key in dict2 and dict1[key] == dict2[key]


def is_changed(key, dict1, dict2):
    return key in dict1 and key in dict2 and dict1[key] != dict2[key]
