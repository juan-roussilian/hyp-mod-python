import textwrap

import click
import requests

from . import __version__



@click.command()
@click.option('--lang', default="en", help='Language desired for the summary.')
@click.version_option(version=__version__)
def main(lang):
    """The hypermodern Python project."""
    url = "https://{}.wikipedia.org/api/rest_v1/page/random/summary".format(lang)
    try:
        with requests.get(url) as response:
            response.raise_for_status()
            data = response.json()
            
    except:
        click.secho("An error ocurred while trying to access wikipedia API. Check if the language characters are valid", fg="red")
        return

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
    