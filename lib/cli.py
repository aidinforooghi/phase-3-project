import click
from db.models import session, Enrollment, Student, Course
from db.seed import seed_data


@click.group()
def cli():
    pass


@cli.command()
def seed_enrollments():
    enrollments = session.query(Enrollment).all()

    for enrollment in enrollments:
        click.echo(f"Student: {enrollment.student.name}, Course: {enrollment.course.name}")


@cli.command()
@click.argument('name')
def add_student(name):

    student = Student(name=name)
    session.add(student)
    session.commit()
    session.close()
    click.echo(f"Added student: {name}")