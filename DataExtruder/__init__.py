import logging
from DataExtruder.datasource import load_data
from DataExtruder.render_data import compile_data
from DataExtruder.helper import get_config, set_var_by_env

logger = logging.getLogger()

def main(template, config="config.json", target="target", log_level="INFO"):
    """Render the data."""
    logging.basicConfig(level=log_level)

    config = get_config(config)
    config = set_var_by_env(config,"DATAEXTRUDER_DIRECTUS_PASSWORD","password")
    config = set_var_by_env(config,"DATAEXTRUDER_DIRECTUS_USERNAME","username")

    data = load_data(config)
    compile_data(template,target, data)
