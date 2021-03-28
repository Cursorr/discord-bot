import json


def load_json(path):
    with open(path, "r") as f:
        config = JsonConfig(path)
        config.content = json.load(f)
        f.close()

    return config


class JsonConfig:
    def __init__(self, path):
        self.path = path
        self.content = dict()

    def write(self):
        with open(self.path, "w") as f:
            f.write(json.dumps(self.content))
            f.close()
