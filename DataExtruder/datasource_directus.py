from DataExtruder.directus_api import DirectusClient
import logging
import os

logger = logging.getLogger()


def transform_data(tranform_config, items):
    for transform_rule in tranform_config:
        transformation_action = transform_rule["action"]
        transformation_field = transform_rule["field"]
        logger.info(f"Transform data based on {transformation_action}")
        for item in items:
            # split a string by newline
            if transformation_action == "split_newline":
                if item[transformation_field]:
                    item[transformation_field] = item[transformation_field].split("\n")
                else:
                    item[transformation_field] = []

            # remove the id field
            if transformation_action == "remove_intermediate_id":
                # new result list
                new_result_list = []

                # check all the elements of the array
                for sub_item in item[transformation_field]:
                    # an go trough all keys, normaly there should be just one _id key.
                    for key in sub_item:
                        # if you found it, attach the value to the new target list
                        if key.endswith("_id"):
                            new_result_list.append(sub_item[key])
                item[transformation_field] = new_result_list

            # rename a field
            if transformation_action == "rename":
                transformation_from = transform_rule["from"]
                transformation_to = transform_rule["to"]
                item[transformation_to] = item[transformation_from]
                del item[transformation_from]
    return items


def load(config):
    client = DirectusClient(
        url=config["url"],
        project="_",
        email=config["username"],
        password=config["password"],
    )
    result = {}
    # Progress data
    for query in config["model"]:
        logger.info(f"Load items for {query['name']}")
        items = client.get_items_list(
            collection_name=query["collection"], fields=query["fields"]
        )[0]
        # for transformation rules, reshape
        if "transform" in query:
            items = transform_data(query["transform"], items)

        result[query["name"]] = items
    return result
