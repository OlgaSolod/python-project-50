import json
import yaml


def parsing(filepath):
    dicti = {}
    if filepath.endswith('.yml') or filepath.endswith('.yaml'):
        dicti = yaml.safe_load(open(filepath))
    elif filepath.endswith('.json'):
        dicti = json.load(open(filepath))
    return dicti


if __name__ == 'main':
    parsing()
