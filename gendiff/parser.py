import json
import yaml


def parse_data(file1, file2):
    if str(file1).endswith('json'):
        dict1 = json.load(open(file1))
        dict2 = json.load(open(file2))
    else:
        dict1 = yaml.safe_load(open(file1))
        dict2 = yaml.safe_load(open(file2))
    return dict1, dict2
