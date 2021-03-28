import json
import os


def load_json(path):
    """
    Load a json configuration from file
    :param path: File to load
    :return: Instance of JsonConfig
    """

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
        """
        Write json config
        """

        with open(self.path, "w") as f:
            f.write(json.dumps(self.content, indent=4))
            f.close()
