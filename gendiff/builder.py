

def make_diff(file1, file2):
    
    def inner_(dicti1, dicti2):
        diff = []
        all_keys = dicti1.keys() | dicti2.keys()
        deleted = dicti1.keys() - dicti2.keys()
        added = dicti2.keys() - dicti1.keys()
        for key in all_keys:
            if isinstance(dicti1.get(key), dict) and isinstance(dicti2.get(key), dict):
                diff.append({
                    'type': 'nested',
                    'key': key,
                    'children': inner_(dicti1.get(key), dicti2.get(key)),
                })
            else:
                if key not in added and key not in deleted:
                    if dicti1.get(key) == dicti2.get(key):
                        diff.append({
                            'type':'unchanged',
                            'key': key,
                            'value': dicti1.get(key),
                        })    
                    else:
                        diff.append({
                            'type': 'changed',
                            'key': key,
                            'value_old': dicti1.get(key),
                            'value_new': dicti2.get(key),
                        })
                elif key in added:
                    diff.append({
                        'type': 'added',
                        'key': key,
                        'value': dicti2.get(key),
                    })
                elif key in deleted:
                    diff.append({
                        'type': 'deleted',
                        'key': key,
                        'value': dicti1.get(key),
                    })
        return diff 
    return inner_(file1, file2)


if __name__ == 'main':
    make_diff()