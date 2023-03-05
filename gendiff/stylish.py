from itertools import chain

def formatter(dicti, space_counts=' ', counter=4):
    def iter_(current_value, depth):
        if not isinstance(current_value, list):
            return str(current_value)
        indent_size = depth + counter  # размер отступа текущего уровня вложенности
        actual_indent = space_counts * (indent_size-2)  # вычисление отступа по формуле 
        previous_indent = space_counts * depth  # это размер предыдущего уровня вложенности
        lines = []
        for elem in current_value:
            for key, val in elem.items():
                if key == 'added':
                    lines.append(f'{actual_indent}+ {iter_(current_value[elem
                                 ], indent_size)}')
                elif] elem == 'removed':
                    lines.append(f'{actual_indent}- {iter_(current_value[elem], indent_size)}')
                elif elem == 'changed':
                    lines.append(f'{actual_indent}- {iter_(current_value[elem], indent_size)}')
                    
                else:
                    lines.append(f'{actual_indent}  {elem}: {iter_(current_value[elem], indent_size)}')
        result = chain('{', lines, [previous_indent +'}'])
        return '\n'.join(result)
    return iter_(dicti, depth=0)

d = [{'common': [{'added': {'follow': False}}, {'setting1': 'Value 1'}, {'removed': {'setting2': 200}}, {'changed': {'setting3': (None, True)}}, {'added': {'setting4': 'blah blah'}}, {'added': {'setting5': {'key5': 'value5'}}}, {'setting6': [{'doge': [{'changed': {'wow': ('so much', '')}}]}, {'key': 'value'}, {'added': {'ops': 'vops'}}]}]}, {'group1': [{'changed': {'baz': ('bars', 'bas')}}, {'foo': 'bar'}, {'changed': {'nest': ('str', {'key': 'value'})}}]}, {'removed': {'group2': {'abc': 12345, 'deep': {'id': 45}}}}, {'added': {'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}]
print(formatter(d))

