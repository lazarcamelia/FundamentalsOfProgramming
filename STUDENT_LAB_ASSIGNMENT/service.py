from domain.student_class import Student
from domain.assignment_class import Assignment
from infrastructure.repository import Repo
from domain.grade_class import Grade
from random import randint
from datetime import datetime

class Service(object):
    def __init__(self, repo_student, repo_assignment, repo_grade):
        self.__repo_student = repo_student
        self.__repo_assignment = repo_assignment
        self.__repo_grade = repo_grade

    def add_student(self, student_id, student_name, student_group):
        """
        function that adds a student to the repository
        :param student_id: int
        :param student_name: string
        :param student_group: int
        :return:
        """
        student = Student(student_id, student_name, student_group)
        self.__repo_student.add(student)

    def list_students(self):
        """
        function that gets from the repository all the students
        :return: list of students
        """
        all_students = self.__repo_student.get_all()
        return all_students

    def remove_student(self, id_student):
        """
        function that search for the id of a student in repository and remove it
        :param id_student: int
        :return: -
        """
        student = Student(id_student, None, None)
        self.__repo_student.remove(student)
        grades = Repo()
        grades = self.__repo_grade.search_for_student(id_student, grades).get_all()

        for grade in grades:
            self.__repo_grade.remove(grade)

    def update_student(self, student_id, student_name, student_group):
        """
        function that update the name and the group of a student
        :param student_id: integer
        :param student_name: string
        :param student_group: integer
        :return: -
        """
       # self.__repo_student.update(student)
        student = Student(student_id, None, None)
        student = self.__repo_student.search(student)
        self.__repo_student.remove(student)
        if student_name is not None:
            student.set_student_name(student_name)
        if student_group is not None:
            student.set_student_group(student_group)
        self.__repo_student.add(student)

    def add_assignment(self, assignment_id, assignment_description, assignment_deadline):
        """
        function that add an assignment to the repository
        :param assignment_id: integer
        :param assignment_description: string
        :param assignment_deadline: string
        :return: -
        """
        assignment = Assignment(assignment_id, assignment_description, assignment_deadline)
        self.__repo_assignment.add(assignment)

    def list_assignments(self):
        """
        function that gets from the repository all the assignments
        :return:
        """
        all_assignments = self.__repo_assignment.get_all()
        return all_assignments

    def update_assignment(self, assignment_id, assignment_description, assignment_deadline):
        """
        function that update the description and the deadline of an assignment
        :param assignment_id: integer
        :param assignment_description: string
        :param assignment_deadline: date
        :return: -
        """
        assignment = Assignment(assignment_id, None, None)
        assignment = self.__repo_assignment.search(assignment)
        self.__repo_assignment.remove(assignment)
        if assignment_description is not None:
            assignment.set_assignment_description(assignment_description)
        if assignment_deadline is not None:
            assignment.set_assignment_deadline(assignment_deadline)
        self.__repo_assignment.add(assignment)
        #self.__repo_assignment.update(assignment)

    def remove_assignment(self, id_assignment):
        """
         function that search for the id of an assignment in repository and remove it
        :param id_assignment: integer
        :return: -
        """
        assignment = Assignment(id_assignment, None, None)
        self.__repo_assignment.remove(assignment)
        grades = Repo()
        grades = self.__repo_grade.search_for_assignments(id_assignment, grades).get_all()

        for grade in grades:
            self.__repo_grade.remove(grade)

    def __get_random_id(self):
        find = False
        while not find:
            id = randint(0, 1000)
            grade = Grade(id, None, None)
            if self.__repo_grade.find(grade) is False:
                return id

    def give_assignment_to_student(self, assignment_id, student_id):
        id_grade = self.__get_random_id()
        grade = Grade(id_grade, student_id, assignment_id)
        if self.__repo_grade.find(grade) is False:
            self.__repo_grade.add(grade)

    def give_assignment_to_group(self, assignment_id, student_group):
        students = Repo()
        students = self.__repo_student.get_after_group(student_group, students).get_all()

        for student in students:
            self.give_assignment_to_student(assignment_id, student.get_id())

    def get_assignments_for_student(self, student_id):
        grades = Repo()
        grades = self.__repo_grade.search_for_student(student_id, grades).get_all()
        assignments = Repo()
        for grade in grades:
            if grade.get_grade() == -1:
                assign = Assignment(grade.get_assignment_id(), None, None)
                assignments.add(self.__repo_assignment.search(assign))
        return assignments.get_all()

    def give_grade(self, student_id, assignment_id, grade_value):
        grade = self.__repo_grade.search_for_grade(student_id, assignment_id)
        if grade.get_grade() == -1:
            self.__repo_grade.remove(grade)
            grade.set_grade(grade_value)
            self.__repo_grade.add(grade)


    def late_students(self):
        today = datetime.today().strftime('%Y.%m.%d')
        grades = self.__repo_grade.get_all()
        students = Repo()
        for grade in grades:
            assign = Assignment(grade.get_assignment_id(), None, None)
            assign = self.__repo_assignment.search(assign)
            date = assign.get_assignment_deadline()
            if date < today and grade.get_grade() == -1:
                student = Student(grade.get_student_id(), None, None)
                if student not in students:
                    student = self.__repo_student.search(student)
                    students.add(student)

        return students.get_all()

    def get_students_for_assignment(self, assignment_id):
        grades = Repo()
        grades = self.__repo_grade.search_for_assignments(assignment_id, grades).get_all()
        students = Repo()
        grades = sorted(grades, key=lambda x: x.get_grade(), reverse=True)
        for grade in grades:
            student_id = grade.get_student_id()
            student = Student(student_id, None, None)
            student = self.__repo_student.search(student)
            students.add(student)
        return students.get_all()




