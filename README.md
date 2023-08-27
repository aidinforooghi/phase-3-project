# Enrollment Management System

Welcome to the Enrollment Management System CLI project! This project demonstrates the use of Python, SQLAlchemy ORM, and Command-Line Interface (CLI) design principles to manage student enrollments in various courses.


## Project Overview

This CLI application allows users to manage student enrollments and courses through a user-friendly command-line interface. It leverages SQLAlchemy ORM for database interactions and follows best practices for CLI design.

## Getting Started

To use this CLI application, follow these steps:

1. Clone this repository to your local machine.
2. Install dependencies using Pipenv: `pipenv install`
3. Activate the virtual environment: `pipenv shell`
4. Create the initial database and seed data: `python cli.py`
5. Run CLI commands as described in the [Commands](#commands) section.

## Commands

The CLI provides the following commands:

```shell
seed_enrollments       # Displays all enrolled students and their courses.
add_student <name>     # Adds a new student with the given name.
add_course <name>      # Adds a new course with the given name.
enroll_student <student_id> <course_id>  # Enrolls a student in a course.
list_students          # Lists all available students.
list_courses           # Lists all available courses.
delete_course <course_id>  # Deletes a course by its ID.
delete_student <student_id> # Deletes a student by their ID.
delete_all_enrollments # Deletes all student enrollments.
generate_report        # Generates a report of all enrollments.
```

## Contributor's Guide
Contributions are welcome! If you'd like to contribute to the Enrollment Management System project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push the changes to your forked repository: `git push origin my-feature-branch`
5. Submit a pull request detailing your changes and their purpose.


## License
The Enrollment Management System project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).


