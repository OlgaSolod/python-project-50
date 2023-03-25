from json import dumps


def format_json(diff):
    return dumps(diff, indent=4)

s = {'common': ('nested', {'follow': ('added', False), 'setting1': ('unchanged', 'Value 1'), 'setting2': ('removed', 200), 'setting3': ('changed', True, None), 'setting4': ('added', 'blah blah'), 'setting5': ('added', {'key5': 'value5'}), 'setting6': ('nested', {'doge': ('nested', {'wow': ('changed', '', 'so much')}), 'key': ('unchanged', 'value'), 'ops': ('added', 'vops')})}), 'group1': ('nested', {'baz': ('changed', 'bas', 'bars'), 'foo': ('unchanged', 'bar'), 'nest': ('changed', {'key': 'value'}, 'str')}), 'group2': ('removed', {'abc': 12345, 'deep': {'id': 45}}), 'group3': ('added', {'deep': {'id': {'number': 45}}, 'fee': 100500})}
print(format_json(s))