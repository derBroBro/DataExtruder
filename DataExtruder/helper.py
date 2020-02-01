import json
import logging
import os

logger = logging.getLogger()


def get_config(filename):
    config = {}
    with open(filename, "r") as f:
        config = json.loads(f.read())
    return config

def save_data(filename, data):
    with open(filename, "w") as f:
        f.write(json.dumps(data, indent=4))

def set_var_by_env(config, env_name, field_name):
    if env_name in os.environ:
        config[field_name] = os.environ[env_name]
    return config