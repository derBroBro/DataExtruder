#!python
import logging
import datasource
import render_data
import helper
import click

logger = logging.getLogger()

@click.command()
@click.option('--log-level', default="INFO", help='Log-Level')
@click.option('--config', default="config.json", help='Config file to use')
@click.option('--target', default="target", help='Where to store the files created')
@click.option('--template', prompt='Which template to use')
def render(log_level, config, target, template):
    """Render the data."""
    logging.basicConfig(level=log_level)

    config = helper.get_config(config)
    config = helper.set_var_by_env(config,"DATAEXTRUDER_DIRECTUS_PASSWORD","password")
    config = helper.set_var_by_env(config,"DATAEXTRUDER_DIRECTUS_username","username")

    data = datasource.get(config)
    render_data.compile(template,target, data)

if __name__ == '__main__':
    render()