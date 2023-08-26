from .models import Student, Course, Enrollment, session

def seed_data():
    student1 = Student(name="John Doe")
    student2 = Student(name="Jane Smith")


        course1 = Course(name="Math")
        course2 = Course(name="Science")

    enrollment1 = Enrollment(student=student1, course=course1)
    enrollment2 = Enrollment(student=student1, course=course2)
    enrollment3 = Enrollment(student=student2, course=course1)

session.add_all([student1, student2, course1, course2, enrollment1, enrollment2, enrollment3])
session.commit()