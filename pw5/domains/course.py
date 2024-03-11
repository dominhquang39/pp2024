class Course:
    def __init__(self, id, name, ects):
        self.__id = id
        self.__name = name
        self.__ects = ects

    def set_id(self, id):
        self.__id = id
     
    def set_name(self, name):
        self.__name = name

    def set_ects(self, ects):
        self.__ects = ects

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_ects(self):
        return self.__ects