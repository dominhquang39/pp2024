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
    def __init__(self, course, student, score):
        self.__course = course
        self.__student = student
        self.__score = score

    def get_student(self):
        return self.__student
    
    def get_course(self):
        return self.__course
    
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
        course = input("Input name of course to assign score: ")
        for student in self.__students:
            score = int(input(f"Input score for {student.get_name()} in {course}: "))
            student_score = Score(course, student, score)
            self.__scores.append(student_score)


    def get_students(self):
        return self.__students
    
    def get_courses(self):
        return self.__courses
    
    def get_num_students(self):
        return self.__num_students
    
    def get_num_courses(self):
        return self.__num_courses
    
    def list_students(self):
        if self.__num_students == 0:
            print("No students yet. Please input students' information first!")
        else: 
            print(f"Total students: {self.get_num_students()} students")
            print("\nList of students: \n")
            for student in self.__students:
                print(f"Name: {student.get_name()}, ID: {student.get_id()}, DOB: {student.get_dob()}")
            print("=====================================================")

    def list_courses(self):
        if self.__num_courses == 0:
            print("No course yet. Please input courses' information first!")
        else:
            print(f"Total courses: {self.get_num_courses()} courses")
            print("\nList of courses: \n")
            for course in self.__courses:
                print(f"Name: {course.get_name()}, ID: {course.get_id()}")
            print("=====================================================")


    def list_scores(self, course_name):
        for course in self.__courses: 
            if course.get_name() == course_name:
                print(f"\nList scores of students in {course.get_name()}: \n")
                for score in self.__scores:
                    if score.get_course() == course_name:
                        print(f"{score.get_student().get_name()}: {score.get_score()}")
                    else:
                        print(f"\nCourse {course_name} not found.")

def main():
    uni = University()

    while(True):
        print("""
            0. Exit
            1. Input students' information
            2. Input courses' information
            3. Input score for specific course
            4. List students' information
            5. List courses'  information
            6. List score of specific course      
        """) 
        option = int(input("Input your choice: "))                                                         
        if option == 0:
            break
        elif option == 1:                                                                            
            uni.set_students()
        elif option == 2:                                                                                                                                 
            uni.set_courses()
        elif option == 3:
            uni.set_scores()
        elif option == 4:
            uni.list_students()
        elif option == 5:
            uni.list_courses()
        else:
            course = input("Input the course to show score: ")
            uni.list_scores(course)

if __name__ == "__main__":
    main()