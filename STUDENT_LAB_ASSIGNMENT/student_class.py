class Student(object):
    def __init__(self, student_id, student_name, student_group):
        """
        function that initialize a student
        :param student_id: integer, id of the student
        :param student_name: string, name of the student
        :param student_group: int, group of the student
        """
        self.__student_id = student_id
        self.__student_name = student_name
        self.__student_group = student_group

    def set_student_name(self, new_name):
        """
        function that modify the name of a student
        :param new_name: string
        :return: -
        """
        self.__student_name = new_name

    def set_student_group(self, new_group):
        """
        function that modify the group of a student
        :param new_group: integer
        :return: -
        """
        self.__student_group = new_group

    def get_id(self):
        """
        function that get the id of a student
        :return: integer
        """
        return self.__student_id

    def get_student_name(self):
        """
        function that get the name of a student
        :return: string
        """
        return self.__student_name

    def get_student_group(self):
        """
        function that get the group of the student
        :return: int
        """
        return self.__student_group

    def __eq__(self, other):
        """
        function that overwrite the equal function
        :param other: object
        :return: true if they have the same id, false otherwise
        """
        return self.get_id() == other.get_id()

    def __str__(self):
        """
        function that overwrites the __str__ function
        :return: a string consisting of all the fields of the object
        """
        return str(self.get_id()) + " " + str(self.get_student_name()) + " " + str(self.get_student_group())