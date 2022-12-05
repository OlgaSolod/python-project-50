import json
from itertools import chain
import copy


def generate_diff(file1, file2):
    indent = ' '*4
    lines = []
    
    f1_copy = copy.deepcopy(file1)
    f2_copy = copy.deepcopy(file2)
    for key1, val1 in file1.items():
        for key2, val2 in file2.items():
            if key1 == key2:
                if val1 == val2:
                    line = f'{indent}{key1}: {val1}'
                    f1_copy.pop(key1)
                    f2_copy.pop(key2)
                    lines.append(line)
    
    for k, v in f1_copy.items():
        lines.append(f'  - {k}: {v}')
    for k, v in f2_copy.items():
        lines.append(f'  + {k}: {v}')
        
    result = chain('{', lines, '}')
    return '\n'.join(result)
path1 = './files/file1.json'
path2 = './files/file2.json'
print(generate_diff(path1, path2))