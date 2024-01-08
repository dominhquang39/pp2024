def input_number_students():
    number = int(input("Input the number of students in this class: "))
    while number <= 0:
        number = int(input("Input again: "))
    return number


def input_student_info():
    students = []
    number = input_number_students()

    for _ in range(number):
        student = {}
        student['Name'] = input("Input name of student: ")
        student['ID'] = input("Input ID of student: ")
        student['DOB'] = input("Input DOB of student: ")
        students.append(student)
    return students


def input_number_courses():
    number =  int(input("Input the number of course: "))
    while (number <= 0):
        number = int(input("Input again: "))
    return number

def input_course_info():
    courses = []
    number = input_number_courses()

    for _ in range(number):
        course = {}
        course['Name'] = input("Input name of course: ")
        course['ID'] = input("Input ID of course: ")
        course.append(course)
    return courses

def input_student_score(students, courses):
    score = []
    
        