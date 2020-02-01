import logging
import helper
import datasource_directus

logger = logging.getLogger()


def get(config, debug_dump=False):
    source_type = config["source_type"]
    data = {}
    if source_type == "directus":
        data = datasource_directus.load(config)
    else:
        logger.error(f"Unknown source kind {source_type}")

    if debug_dump:
        helper.save_data("dump.json", data)
    return data
