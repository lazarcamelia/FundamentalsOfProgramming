from business.service import  Service
from infrastructure.repository import Repo
from UI.console import UI
from random import randint
from domain.assignment_class import Assignment
from domain.student_class import Student
from errors.error import RepoError

def initialize_students(Repo_Student):
    List = ["Ana", "Maria", "Gheorghe", "Alice", "Jackson", "Moris", "Diana", "Angela", "Michael", "Alec"]

    for i in range(12):
        student_id = randint(1, 100)
        student_name = List[randint(0, 9)]
        student_group = randint(1, 100)

        student = Student(student_id, student_name, student_group)
        if Repo_Student.find(student) is False:
            Repo_Student.add(student)

    return Repo_Student

def initialize_assignments(Repo_Assignment):
    Dates = ["2019.10.10", "2019.11.10", "2019.11.15", "2020.11.23", "2019.10.12", "201911.12", "2019.07.12", "2020.10.20", "2020.02.02", "2020.02.12"]
    Descr = ["homework1", "homework2", "homework3", "homework4", "homework5", "homework6", "homework7", "homework8", "homework9", "homework10"]
    for i in range(10):
        try:
            assignment_id = randint(1, 100)
            assignment_description = Descr[randint(0, 9)]
            assignment_deadline = Dates[randint(0, 9)]
            Repo_Assignment.add(Assignment(assignment_id, assignment_description, assignment_deadline))
        except RepoError:
            continue
    return Repo_Assignment


if __name__ == "__main__":
    Repo_Student = Repo()
    Repo_Assignment = Repo()
    Repo_Grade = Repo()

    Repo_Student = initialize_students(Repo_Student)
    Repo_Assignment = initialize_assignments(Repo_Assignment)

    Service_Lab = Service(Repo_Student, Repo_Assignment, Repo_Grade)
    ui = UI(Service_Lab)
    ui.run()
