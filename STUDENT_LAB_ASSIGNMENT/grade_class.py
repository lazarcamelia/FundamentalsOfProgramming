class Grade(object):
    def __init__(self, grade_id, student_id, assignment_id):
        self.__grade_id = grade_id
        self.__student_id = student_id
        self.__assignment_id = assignment_id
        self.__grade = -1

    def set_grade(self, new_grade):
        """
        function that set the grade of an assignment only if it was not setted before
        :param new_grade: integer between 1 and 10
        :return: -
        """
        if self.get_grade() == -1:
            self.__grade = new_grade

    def get_id(self):
        """
        function that gets the id of a grade
        :return:
        """
        return self.__grade_id

    def get_assignment_id(self):
        """
        function that gets the id of the assignment of a given grade
        :return: integer
        """
        return self.__assignment_id

    def get_student_id(self):
        """
        function that gets the id of the student of a given grade
        :return: integer
        """
        return self.__student_id

    def get_grade(self):
        """
        function that gets a grade
        :return: integer
        """
        return self.__grade

    def __str__(self):
        """
         function that overwrites the __str__ function
        :return: a string consisting of all the fields of the object
        """
        return str(self.get_id()) + " " + str(self.get_student_id()) + " " + str(self.get_assignment_id())

    def __eq__(self, other):
        """
        function that overwrite the equal function
        :param other: object
        :return: true if they have the same id, false otherwise
        """
        return self.get_id() == other.get_id()