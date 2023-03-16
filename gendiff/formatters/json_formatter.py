from json import dumps


def make_json(diff):
    return dumps(diff, indent=4)
