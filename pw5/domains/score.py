import math
class Score:
    def __init__(self, course, student, score):
        self.__course = course
        self.__student = student
        self.__score = score

    def get_student(self):
        return self.__student
    
    def get_course(self):
        return self.__course
    
    def get_score(self):
        return math.floor((self.__score*10)/10)