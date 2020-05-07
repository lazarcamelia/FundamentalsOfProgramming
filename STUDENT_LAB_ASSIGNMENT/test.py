import unittest

from domain.student_class import Student
from domain.assignment_class import Assignment
from domain.grade_class import Grade
from errors.error import RepoError, ValidError
from infrastructure.repository import Repo


class Tests_First_Functionality(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_student(self):
        s_id = 3
        name = "ana"
        group = 95
        student = Student(s_id, name, group)
        assert(student.get_id() == 3)
        assert(student.get_student_name() == "ana")
        assert(student.get_student_group() == 95)
        student.set_student_name("blana")
        assert(student.get_student_name() == "blana")
        dif_student_same_id = Student(3, "iarna", 57)
        assert(student == dif_student_same_id)

    def test_update_student(self):
        s_id = 3
        name = "ana"
        group = 95
        student = Student(s_id, name, group)
        student.set_student_name("lola")
        assert (student.get_student_name() == "lola")
        student.set_student_group(914)
        assert (student.get_student_group() == 914)

    def test_remove_student(self):
        students = Repo()
        student1 = Student(1, "ana", 911)
        student2 = Student(2, "alina", 912)
        students.add(student1)
        students.add(student2)
        assert (students.size() == 2)
        students.remove(student1)
        assert (students.size() == 1)

    def test_create_assignment(self):
        a_id = 1
        description = "homework"
        deadline = "10-10-2010"
        assignment = Assignment(a_id, description, deadline)
        assert (assignment.get_id() == 1)
        assert (assignment.get_assignment_description() == description)
        assert (assignment.get_assignment_deadline() == deadline)
        assignment.set_assignment_description("tema")
        assert (assignment.get_assignment_description() == "tema")
        dif_assign_same_id = Assignment(1, "diefie", "10.10.2000")
        assert (assignment == dif_assign_same_id)

    def test_update_assignment(self):
        a_id = 1
        description = "homework"
        deadline = "10-10-2010"
        assignment = Assignment(a_id, description, deadline)
        assignment.set_assignment_description("lola")
        assert (assignment.get_assignment_description() == "lola")
        assignment.set_assignment_deadline("20.12.2019")
        assert (assignment.get_assignment_deadline() == "20.12.2019")

    def test_remove_assignment(self):
        assignments = Repo()
        assignment1 = Assignment(1, "fiejfe", "01.01.2020")
        assignment2 = Assignment(2, "frijfr", "10.10.2000")
        assignments.add(assignment1)
        assert (assignments.size() == 1)
        assignments.add(assignment2)
        assert (assignments.size() == 2)
        assignments.remove(assignment2)
        assert (assignments.size() == 1)
        assignments.remove(assignment1)
        assert (assignments.size() == 0)

    def test_repo_student_add_search(self):
        repo = Repo()
        assert (repo.size() == 0)
        student = Student(3, "ana", 95)
        dif_student_same_id = Student(3, "iarna", 57)
        repo.add(student)
        assert (repo.size() == 1)
        keyStudent = Student(student.get_id(), None, None)
        foundStudent = repo.search(keyStudent)
        assert (foundStudent.get_student_name() == student.get_student_name())
        try:
            repo.add(dif_student_same_id)
            assert(False)
        except RepoError as re:
            assert (str(re) == "Element already exist!")
        inexisting_student = Student(24, "kobe", 50)
        try:
            repo.search(inexisting_student)
            assert (False)
        except RepoError as re:
            assert (str(re) == "Inexisting element")
        students = repo.get_all()
        assert (students == [student])
