import click
from db.models import session, Enrollment
from db.seed import seed_data


@click.group()
def cli():
    pass



@cli.command()
def enrollments():
    enrollments = session.query(Enrollment).all()



    for enrollment in enrollments:
        click.echo(f"Student: {enrollment.student.name}, Course: {enrollment.course.name}")



if __name__ == "__main__":
    seed_data()
    cli()