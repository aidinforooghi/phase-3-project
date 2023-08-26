import click
from db.models import session, Enrollment
from db.seed import seed_data


@click.group()
def cli():
    pass



@cli.command()