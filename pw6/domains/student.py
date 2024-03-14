class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def set_id(self, id):
        self.__id = id
     
    def set_name (self, name):
        self.__name = name

    def set_dob (self, dob):
        self.__dob = dob

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob