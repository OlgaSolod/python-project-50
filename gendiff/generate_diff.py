from gendiff.reading import reading_files
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json_formatter import format_json


def generate_diff(path1, path2, format='stylish'):
    dict1, dict2 = reading_files(path1, path2)
    if format == 'stylish':
        return format_stylish(build_tree(dict1, dict2))
    elif format == 'plain':
        return format_plain(build_tree(dict1, dict2))
    elif format == 'json':
        return format_json(build_tree(dict1, dict2))


def build_tree(dict1, dict2):
    diff = {}
    for key in sorted(set(dict1.keys()) | set(dict2.keys())):
        if is_removed(key, dict1, dict2):
            diff[key] = ('removed', dict1[key])
        elif is_added(key, dict1, dict2):
            diff[key] = ('added', dict2[key])
        elif is_changed(key, dict1, dict2):
            if is_nested(key, dict1, dict2):
                diff[key] = ('nested', build_tree(dict1[key], dict2[key]))
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


def is_nested(key, dict1, dict2):
    return is_dict(dict1[key]) and is_dict(dict2[key])

# dict1, dict2 = reading_files('tests/fixtures/nested1.json', 'tests/fixtures/nested2.json')
# dict1 = {'common': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {'key': 'value', 'doge': {'wow': ''}}}, 'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}}, 'group2': {'abc': 12345, 'deep': {'id': 45}}}
# dict2 = {'common': {'follow': False, 'setting1': 'Value 1', 'setting3': None, 'setting4': 'blah blah', 'setting5': {'key5': 'value5'}, 'setting6': {'key': 'value', 'ops': 'vops', 'doge': {'wow': 'so much'}}}, 'group1': {'foo': 'bar', 'baz': 'bars', 'nest': 'str'}, 'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}
# print(build_tree(dict1, dict2))