from errors.error import RepoError, CommandError
from validators.validator_class import Validator

class UI(object):
    def __init__(self, service):
      #  self.__validator = Validator()
        self.__service = service
        self.__commands ={
            "1":self.__ui_student,
            "1.1":self.__ui_add_student,
            "1.2":self.__ui_remove_student,
            "1.3":self.__ui_update_student,
            "1.3.1":self.__ui_update_name_student,
            "1.3.2":self.__ui_update_group_student,
            "1.4":self.__ui_list_students,
            "2":self.__ui_assignment,
            "2.1":self.__ui_add_assignment,
            "2.2":self.__ui_remove_assignment,
            "2.3":self.__ui_update_assignment,
            "2.3.1":self.__ui_update_description_assignment,
            "2.3.2":self.__ui_update_deadline_assignment,
            "2.4":self.__ui_list_assignments,
            "3":self.__ui_give_assignment,
            "3.1":self.__ui_give_to_student_assignment,
            "3.2":self.__ui_give_to_group_assignment,
            "4":self.__ui_grade_student,
            "5":self.__ui_statistics,
            "5.1":self.__ui_list_students_for_assignment,
            "5.2":self.__ui_list_students_late,
            "6":self.__exit
        }

    def __ui_student(self):
        print("Choose 1 of the functionalities below:")
        print("1.1. Add a new student")
        print("1.2. Remove a student")
        print("1.3. Update a student")
        print("1.4. List the students")
        cmd = input("Your command is = ")
        if cmd in self.__commands:
            self.__commands[cmd]()
        else:
            raise CommandError("Invalid command")

    def __ui_add_student(self):
        student_id = int(input("Give the id of the student = "))
        student_name = input("Give the name of the student = ")
        student_group = int(input("Give the group of the student = "))
        #self.__validator.validate_student(student)
        self.__service.add_student(student_id, student_name, student_group)

    def __ui_remove_student(self):
        self.__ui_list_students()
        student_id = int(input("Give the id of the students to be removed = "))
        self.__service.remove_student(student_id)

    def __ui_update_student(self):
        self.__ui_list_students()
        student_id = int(input("Give the id of the students to be updated = "))
        print("1.3.1. Update the name of the student")
        print("1.3.2. Update the group of the student")
        cmd = input("Your command is = ")
        if cmd in self.__commands:
            self.__commands[cmd](student_id)
        else:
            raise CommandError("Invalid command")

    def __ui_update_name_student(self, student_id):
        student_name = input("Write the new name of the student = ")
        student_group = None
        self.__service.update_student(student_id, student_name, student_group)

    def __ui_update_group_student(self, student_id):
        student_group = int(input("Give the new group of the student = "))
        student_name = None
        self.__service.update_student(student_id, student_name, student_group)

    def __ui_list_students(self):
        all_students = self.__service.list_students()
        for student in all_students:
            print(student)

    def __ui_assignment(self):
        print("Choose 1 of the functionalities below:")
        print("2.1. Add a new assignment")
        print("2.2. Remove an assignment")
        print("2.3. Update an assignment")
        print("2.4. List the assignments")
        cmd = input("Your command is = ")
        if cmd in self.__commands:
            self.__commands[cmd]()
        else:
            raise CommandError("Invalid command")

    def __ui_add_assignment(self):
        assignment_id = int(input("Give the id of the assignment = "))
        assignment_description = input("Give the description of the assignment = ")
        assignment_deadline = int(input("Give the deadline of the assignment = "))
        #self.__validator.validate_assignment(assignment)
        self.__service.add_assignment(assignment_id, assignment_description, assignment_deadline)

    def __ui_remove_assignment(self):
        self.__ui_list_assignments()
        assignment_id = int(input("Give the id of the assignment to be removed = "))
        self.__service.remove_assignment(assignment_id)

    def __ui_list_assignments(self):
        all_assignments = self.__service.list_assignments()

        for assignment in all_assignments:
            print(assignment)

    def __ui_update_assignment(self):
        self.__ui_list_assignments()
        assignment_id = int(input("Give the id of the assignment to be updated = "))
        print("2.3.1. Update the description of the assignment")
        print("2.3.2. Update the deadline of the assignment")
        cmd = input("Your command is = ")
        if cmd in self.__commands:
            self.__commands[cmd](assignment_id)
        else:
            raise CommandError("Invalid command")

    def __ui_update_description_assignment(self, assignment_id):
        assignment_description = input("Write the new description of the assignment = ")
        assignment_deadline = None
        self.__service.update_assignment(assignment_id, assignment_description, assignment_deadline)

    def __ui_update_deadline_assignment(self, assignment_id):
        assignment_deadline = input("Write the new deadline of the assignment = ")
        assignment_description = None
        self.__service.update_assignment(assignment_id, assignment_description, assignment_deadline)

    def __ui_give_assignment(self):
        self.__ui_list_assignments()
        assignment_id = int(input("Give the id of the assignment to be given = "))
        print("3.1. Give the assignment to a student")
        print("3.2. Give the assignment to a group of students")
        cmd = input("Your command is = ")
        if cmd in self.__commands:
            self.__commands[cmd](assignment_id)
        else:
            raise CommandError("Invalid command")

    def __ui_give_to_student_assignment(self, assignment_id):
        student_id = int(input("Give the id of the student to be given the assignment = "))
        self.__service.give_assignment_to_student(assignment_id, student_id)

    def __ui_give_to_group_assignment(self, assignment_id):
        student_group = int(input("Give the group of the students to be given the assignment = "))
        self.__service.give_assignment_to_group(assignment_id, student_group)

    def __ui_print_assignments_for_student(self, student_id):
        all_students = self.__service.get_assignments_for_student(student_id)
        for student in all_students:
            print(student)

    def __ui_grade_student(self):
        student_id = int(input("Give the id of the student to be graded = "))
        self.__ui_print_assignments_for_student(student_id)
        assignment_id = int(input("Give the id of the assignment to be graded = "))
        grade = int(input("Give the grade for the assignment = "))
        self.__service.give_grade(student_id, assignment_id, grade)

    def __ui_statistics(self):
        print("What statistics would you like to see?")
        print("5.1. Print all students who received a given assignment")
        print("5.2. Print all students who are late in handling at least one assignment")
        cmd = input("Your command is = ")

        if cmd in self.__commands:
            self.__commands[cmd]()
        else:
            raise CommandError("Invalid command")

    def __ui_list_students_for_assignment(self):
        assignment_id = int(input("Give the id of the assignment = "))
        students = self.__service.get_students_for_assignment(assignment_id)
        for student in students:
            print(student)

    def __ui_list_students_late(self):
        students = self.__service.late_students()

        for student in students:
            print(student)

    def __exit(self):
        pass

    def run(self):
        finished = False
        while not finished:
            try:
                print("Choose one of the functionalities below:")
                print("1. Add, remove, update or list students")
                print("2. Add, remove, update or list assignments")
                print("3. Give an assignment to a student or a group of students")
                print("4. Grade a student for a given assignment")
                print("5. Print statistics")
                print("6. Exit")

                cmd = input("Your command is = ")
                if cmd in self.__commands:
                    self.__commands[cmd]()
                else:
                    raise CommandError("Invalid command")

            except RepoError as re:
                print(re)
            except ValueError:
                print("The program requires another type of data")
            except CommandError as ce:
                print(ce)