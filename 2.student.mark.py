class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def set_id (self, id):
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

class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def set_id (self, id):
        self.__id = id
     
    def set_name (self, name):
        self.__name = name
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

class Score:
    def __init__(self, course, student):
        self.__course = course
        self.__student = student
        self.__score = int(input(f"Enter the score of {self.__course} of {self.__student}: "))
    
    def get_score(self):
        return self.__score

class University:
    def __init__(self):
        self.__num_students = 0
        self.__num_courses = 0
        self.__students = []
        self.__courses = []
        self.__scores = []
    
    def set_students(self):
        self.__num_students = int(input("Input total number of students: "))
        for _ in range (self.__num_students):
            id = input("Input ID of student: ")
            name = input("Input name of student: ")
            dob = input("Input day of birth of student: ")
            student = Student(id, name, dob)
            self.__students.append(student)

    def set_courses(self):
        self.__num_courses = int(input("Input total number of courses: "))
        for _ in range (self.__num_courses):
            id = input("Input ID of course: ")
            name = input("Input name of course: ")
            course = Course(id, name)
            self.__courses.append(course)

    def set_scores(self):
        course = int(input("Input name of course to assign score for students: "))
        for _ in range (self.__num_students):
            score = Score(course, self.get_students())
            self.__scores.append(score)
        

    def get_num_students(self):
        if self.__num_students == 0:
            return "No student yet!"
        return self.__num_students
    
    def get_num_courses(self):
        if self.__num_students == 0:
            return "No course yet!"
        return self.__num_courses

    
    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def list_students(self):
        print("Lists of students: ")
        Utils.show(self.get_students())

    # Display a list of courses
    def list_courses(self):
        print("Course list: ")
        Utils.show(self.get_courses())

# Main function for the "game"
def main():
    univ = University()

    while(True):
        print("""
    0. Exit
    1. 
    2. 
    ...
    n
    """) 
        option = int(input("Your choice: "))                                                         # Choose option from 0 -> n
        if option == 0:
            break

        elif option == 1:                                                                            # Option 1
            univ.set_students()
        elif option == 2:                                                                            # Option 2                                                     
            univ.set_courses()
        ... ... 

        elif option == n:                                                                            # Option n
            # last function (your choice)
            # univ.list_students() or univ.list_courses()
        else:
            print("Invalid input. Please try again!")


# Call the main function
if __name__ == "__main__":
    main()