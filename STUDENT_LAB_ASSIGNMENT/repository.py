from errors.error import RepoError

class Repo(object):
    def __init__(self):
        self.__entities = []

    def size(self):
        return len(self.__entities)

    def add(self, element):
        """
        function that adds a new element to the repository
        :param element: student/assignment/grade
        :return: -
        """
        if element not in self.__entities:
            self.__entities.append(element)
        else:
            raise RepoError("Element already exist!")

    def remove(self, element):
        """
        function that removes an element from repository
        :param element: student/assignment/grade
        :return: -
        """
        if element not in self.__entities:
            raise RepoError("Inexisting element")
        self.__entities.remove(element)

    def search(self, element):
        """
        function that search for an element in repository
        :param element: student/assignment/grade
        :return: -
        """
        if element not in self.__entities:
            raise RepoError("Inexisting element")
        for elem in self.__entities:
            if elem == element:
                return elem

    def find(self, element):
        """
        function that search for an element in repository
        :param element: student/assignment/grade
        :return: True if is in repo, false otherwise
        """
        if element in self.__entities:
            return True
        return False

    def get_all(self):
        """
        function that returns all the elements from repository
        :return: list of objects
        """
        return self.__entities[:]

    def get_after_group(self, group, return_list):
        for element in self.__entities:
            if element.get_student_group() == group:
                return_list.add(element)
        return return_list

    def search_for_assignments(self, assignment_id, return_list):
        for element in self.__entities:
            if element.get_assignment_id() == assignment_id:
                return_list.add(element)
        return return_list

    def search_for_student(self, student_id, return_list):
        for element in self.__entities:
            if element.get_student_id() == student_id:
                return_list.add(element)
        return return_list

    def search_for_grade(self, student_id, assignment_id):
        for element in self.__entities:
            if element.get_student_id() == student_id and element.get_assignment_id() == assignment_id:
                return element