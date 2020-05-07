class Assignment(object):
    def __init__(self, assignment_id, assignment_description, assignment_deadline):
        """
        function that initialize an assignment
        :param assignment_id: integer, id of the assignment
        :param assignment_description: string, description of an assignment
        :param assignment_deadline: string, the deadline of an assignment
        """
        self.__assignment_id = assignment_id
        self.__assignment_description = assignment_description
        self.__assignment_deadline = assignment_deadline

    def set_assignment_description(self, new_description):
        """
        function that modify the name of an assignemnt
        :param new_description: string
        :return: -
        """
        self.__assignment_description = new_description

    def set_assignment_deadline(self, new_deadline):
        """
        function that modify the deadline of an assignment
        :param new_deadline: string
        :return: -
        """
        self.__assignment_deadline = new_deadline

    def get_id(self):
        """
        function that get the id of an assignment
        :return: integer
        """
        return self.__assignment_id

    def get_assignment_description(self):
        """
        function that get the name of an assignment
        :return: string
        """
        return self.__assignment_description

    def get_assignment_deadline(self):
        """
        function that get the deadline of an assignment
        :return: deadline
        """
        return self.__assignment_deadline

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
        return str(self.get_id()) + " " + self.get_assignment_description() + " " + self.get_assignment_deadline()