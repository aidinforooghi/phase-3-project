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

@cli.command()
@click.argument('name')
def add_course(name):

    course = Course(name=name)
    session.add(course)
    session.commit()
    session.close()
    click.echo(f"Added course: {name}")

@cli.command()
@click.argument('student_id', type=int)
@click.argument('course_id', type=int)
def enroll_student(student_id, course_id):

    student = session.query(Student).get(student_id)
    course = session.query(Course).get(course_id)

    if not student or not course:
        click.echo("Invalid student ID or course ID")
    else:
        course_name = course.name
        student_name = student.name
        enrollment = Enrollment(student=student, course=course)
        session.add(enrollment)
        session.commit()
        session.close()
        message = f"Enrolled student {student_name} in course {course_name}"
        click.echo(message)

@cli.command()
def list_students():

    students = session.query(Student).all()

    if not students:
        click.echo("No students found.")
    else:
        click.echo("Students:")
        for student in students:
            click.echo(f"ID: {student.id} | Name: {student.name}")

    session.close()