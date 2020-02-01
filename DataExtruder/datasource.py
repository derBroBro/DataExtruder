import logging
from DataExtruder.helper import save_data

logger = logging.getLogger()


def load_data(config, debug_dump=False):
    source_type = config["source_type"]
    data = {}
    if source_type == "directus":
        from DataExtruder.datasource_directus import load
        data = load(config)
    else:
        logger.error(f"Unknown source kind {source_type}")

    if debug_dump:
        save_data("dump.json", data)
    return data
