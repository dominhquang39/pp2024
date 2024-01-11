def input_number_students():
    number = int(input("Input the number of students in this class: "))
    while number <= 0:
        number = int(input("Input again: "))
    return number


def input_student_info(num_students):
    students = []
    for _ in range(num_students):
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

def input_course_info(num_courses):
    courses = []

    for _ in range(num_courses):
            course = {}
            course['Name'] = input("Input name of course: ")
            course['ID'] = input("Input ID of course: ")
            courses.append(course)
    return courses

def input_student_score(students, course):
    print(f"Input score for the student in course {course}: ")
    scores = []
    for student in students:
        score = float(input(f"Input score for student {student['Name']}: "))
        studentScore = {
            'StudentName' : student['Name'],
            'Course' : course,
            'Score' : score
        }
        scores.append(studentScore)

    return scores

def list_student (students):  
    if len(students) == 0:
        print("No student yet")
    else:
        print ("\nList of students: \n")
        for student in students:
            print(f"Name: {student['Name']}, ID: {student['ID']}, DOB: {student['DOB']}")

def list_course (courses):
    if len(courses) == 0:
        print("No course yet")
    else:
        print("\nList of course: \n")
        for course in courses:
            print(f"Name: {course['Name']}, ID: {course['ID']}")
        
def list_score_of_course (course, scores):
    print(f"List score of students in course {course}: ")
    if not scores:
        print("No score yet")
    else:
        for score in scores:
            print(f"{score['StudentName']}: {score['Score']}")

def main():
    students = []
    courses = []
    scores = []
    while (True):
        print ("""
        Student managment: 
        0. Exit
        1. Input students information 
        2. Input course information
        3. Input score for specific course
        4. List students information
        5. List courses information
        6. List scores of specific course""")
    
        option = int(input("\nInput your choice: "))
        while option < 0 or option > 6:
            option = int(input("Input your choice again: "))
        
        if option == 0:
            break
        elif option == 1:
            num_students = input_number_students()
            students = input_student_info(num_students)
        elif option == 2:
            num_courses = input_number_courses()
            courses = input_course_info(num_courses)
        elif option == 3:
            if not students or not courses:
                print("Input student and course information first.")
            else: 
                course = input("Input the course to input score: ")
                scores.extend(input_student_score(students, course))
        elif option == 4:
            list_student(students)
        elif option == 5:
            list_course(courses)
        else:
            if not students or not courses:
                print("Please input student and course information first.")
            else:
                course = input("Input the course to show score: ")
                list_score_of_course(course, scores)

if __name__ == "__main__":
    main()  