from itertools import chain

# функция которая будет раскрывать нераскрытые словари
def stringify_value(value, space_counts = ' ', counter=4):
    def iter_(cur_value, depth):
        if not isinstance(cur_value, dict):
            return change_value(cur_value)
        lines = []
        indent_size = counter + depth
        actual_indent = space_counts * (indent_size-2)
        current_indent = space_counts * depth
        for key, val in cur_value.items():
            
            lines.append(f'{actual_indent}  {key}: {iter_(val, indent_size)}')
            
        result = chain('{', lines, [current_indent +'}'])
        return '\n'.join(result)
    return iter_(value, depth=4)


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
                    lines.append(f'{actual_indent}+ {key}: {stringify_value(val[1])}')
                elif val[0] == 'removed':
                    lines.append(f'{actual_indent}- {key}: {stringify_value(val[1])}')
                elif val[0] == 'changed':
                    lines.append(f'{actual_indent}- {key}: {stringify_value(val[1])}')
                    lines.append(f'{actual_indent}+ {key}: {stringify_value(val[2])}')
                elif val[0] == 'unchanged':
                    lines.append(f'{actual_indent}  {key}: {stringify_value(val[1])}')
            else:
                lines.append(f'{actual_indent}  {key}: {stringify_value(iter_(val, indent_size))}')
        result = chain('{', lines, [previous_indent +'}'])
        return '\n'.join(result)
    return iter_(value, 0)

def change_value(value):
    if isinstance(value, (str, bool, int)):
        return str(value).lower()
    elif value == None:
        return 'null'

# s = {'nest': {
#         'key': 'value'
#     }}
# l = [{'common': [{'removed': {'follow': False}}, {'setting1': 'Value 1'}, {'added': {'setting2': 200}}, {'changed': {'setting3': (None, True)}}, {'removed': {'setting4': 'blah blah'}}, {'removed': {'setting5': {'key5': 'value5'}}}, {'setting6': [{'doge': [{'changed': {'wow': ('so much', '')}}]}, {'key': 'value'}, {'removed': {'ops': 'vops'}}]}]}, {'group1': [{'changed': {'baz': ('bars', 'bas')}}, {'foo': 'bar'}, {'changed': {'nest': ('str', {'key': 'value'})}}]}, {'added': {'group2': {'abc': 12345, 'deep': {'id': 45}}}}, {'removed': {'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}]
# # d = {'common': {'follow': ('added', False), 'setting1': 'Value 1', 'setting2': ('removed', 200), 'setting3': ('changed', True, None), 'setting4': ('added', 'blah blah'), 'setting5': ('added', {'key5': 'value5'}), 'setting6': {'doge': {'wow': ('changed', '', 'so much')}, 'key': 'value', 'ops': ('added', 'vops')}}, 'group1': {'baz': ('changed', 'bas', 'bars'), 'foo': 'bar', 'nest': ('changed', {'key': 'value'}, 'str')}, 'group2': ('removed', {'abc': 12345, 'deep': {'id': 45}}), 'group3': ('added', {'deep': {'id': {'number': 45}}, 'fee': 100500})}
# plain = [{'removed': {'follow': False}}, {'host': 'hexlet.io'}, {'removed': {'proxy': '123.234.53.22'}}, {'changed': {'timeout': (50, 20)}}, {'added': {'verbose': True}}]
# d = {'common': {'follow': ('added', False), 'setting1': ('unchanged', 'Value 1'), 'setting2': ('removed', 200), 'setting3': ('changed', True, None), 'setting4': ('added', 'blah blah'), 'setting5': ('added', {'key5': 'value5'}), 'setting6': {'doge': {'wow': ('changed', '', 'so much')}, 'key': ('unchanged', 'value'), 'ops': ('added', 'vops')}}, 'group1': {'baz': ('changed', 'bas', 'bars'), 'foo': ('unchanged', 'bar'), 'nest': ('changed', {'key': 'value'}, 'str')}, 'group2': ('removed', {'abc': 12345, 'deep': {'id': 45}}), 'group3': ('added', {'deep': {'id': {'number': 45}}, 'fee': 100500})}
# print(formatter(d))
#formatter(d)


