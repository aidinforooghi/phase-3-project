from .models import Student, Course, Enrollment, session

def seed_data():
    student1 = Student(name="John Doe")
    student2 = Student(name="Jane Smith")