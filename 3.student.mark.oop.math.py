import math
import numpy as np
import curses
from curses import wrapper



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
    
    # def get_GPA(self, scores, total_ects):
    #     sum = 0
    #     for score in scores:
    #         if score.get_student() == self:
    #             sum += score.get_course().get_ects() * score.get_score()

    #     if total_ects == 0:
    #         return 0.0     
            
    #     gpa = sum / total_ects
    #     return round(gpa, 1)

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
    
def get_user_input(stdscr, user_input):
    stdscr.clear()
    stdscr.addstr(0, 0, user_input)
    stdscr.refresh()
    curses.echo()
    user_data = stdscr.getstr().decode("utf-8")
    curses.noecho()
    return user_data


class University:
    def __init__(self):
        self.__num_students = 0
        self.__num_courses = 0
        self.__students = []
        self.__courses = []
        self.__scores = []

    def set_num_students(self, stdscr):
        while (True):
            try:
                self.__num_students = int(get_user_input(stdscr, "Input total number of students: "))
                stdscr.refresh()
                if self.__num_students > 0:
                    return self.__num_students
                else:
                    stdscr.attron(curses.color_pair(3))
                    stdscr.addstr("Invalid value! Please input positive number of students!")
                    stdscr.attroff(curses.color_pair(3))
                    stdscr.refresh()
                    stdscr.getch()
            except ValueError:
                stdscr.attron(curses.color_pair(3))
                stdscr.addstr("Invalid value. Please input positive number of students!")
                stdscr.attroff(curses.color_pair(3))
                stdscr.refresh()
                stdscr.getch()
    
    def set_students(self, stdscr):
        num_students = self.set_num_students(stdscr)
        for _ in range (num_students):
            id = get_user_input(stdscr, "Input ID of student: ")
            stdscr.refresh()
            name = get_user_input(stdscr, "Input name of student: ")
            stdscr.refresh()
            dob = get_user_input(stdscr, "Input day of birth of student: ")
            stdscr.refresh()
            student = Student(id, name, dob)
            self.__students.append(student)

    def set_num_courses(self, stdscr):
        while (True):
            try:
                self.__num_courses = int(get_user_input(stdscr, "Input total number of courses: "))
                stdscr.refresh()
                if self.__num_courses > 0:
                    return self.__num_courses
                else:
                    stdscr.attron(curses.color_pair(3))
                    stdscr.addstr("Invalid value! Please input positive number of courses!")
                    stdscr.attroff(curses.color_pair(3))
                    stdscr.refresh()
                    stdscr.getch()
            except ValueError:
                stdscr.addstr("Invalid value. Please input positive number of courses!")
                stdscr.refresh()
                stdscr.getch()


    def set_courses(self, stdscr):
        num_courses = self.set_num_courses(stdscr)
        for _ in range (num_courses):
            id = get_user_input(stdscr, "Input ID of course: ")
            stdscr.refresh()
            name = get_user_input(stdscr, "Input name of course: ")
            stdscr.refresh()
            ects = int(get_user_input(stdscr, "Input ects for course: "))
            stdscr.refresh()
            course = Course(id, name, ects)
            self.__courses.append(course)  
            
    def set_scores(self, stdscr):
        course_name = get_user_input(stdscr, "Input name of course to assign score: ")
        stdscr.refresh()
        course = self.get_course_by_name(course_name)

        if course is None:
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr(f"Course '{course_name}' not found")
            stdscr.attroff(curses.color_pair(3))
            stdscr.refresh()
            stdscr.getch()
            return 
        
        for student in self.__students:
            score = float(get_user_input(stdscr, f"Input score for {student.get_name()} in {course_name}: "))
            stdscr.refresh()
            stdscr.getch()
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
    
    # def get_total_ects(self):
    #     total_ects = 0
    #     for course in self.__courses:
    #         total_ects += course.get_ects()
    #     return total_ects
    
    def list_students(self, stdscr):
        if self.__num_students == 0:
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr("No students yet. Please input students' information first!")
            stdscr.attroff(curses.color_pair(3))
            stdscr.refresh()
            stdscr.getch()
        else: 
            stdscr.addstr(f"Total students: {self.get_num_students()} students")
            stdscr.addstr("\nList of students: \n")
            for student in self.__students:
                stdscr.addstr(f"Name: {student.get_name()}, ID: {student.get_id()}, DOB: {student.get_dob()}\n")
            stdscr.addstr("=====================================================")
            stdscr.refresh()
            stdscr.getch()
            

    def list_courses(self, stdscr):
        if self.__num_courses == 0:
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr("No course yet. Please input courses' information first!")
            stdscr.attroff(curses.color_pair(3))
            stdscr.refresh()
            stdscr.getch()
        else:
            stdscr.addstr(f"Total courses: {self.get_num_courses()} courses")
            stdscr.addstr("\nList of courses: \n")
            for course in self.__courses:
                stdscr.addstr(f"Name: {course.get_name()}, ID: {course.get_id()}, ECTS: {course.get_ects()}\n")
            stdscr.addstr("=====================================================")
            stdscr.refresh()
            stdscr.getch()

    def list_scores(self, stdscr):
        if self.__num_students == 0 or self.__num_courses == 0:
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr("Input students' and courses' information first!")
            stdscr.attroff(curses.color_pair(3))
            stdscr.refresh()
            stdscr.getch()
        elif not self.__scores:
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr("No score yet! Please input score for students in this course first!")
            stdscr.attroff(curses.color_pair(3))
            stdscr.refresh()
            stdscr.getch()
        else:
            course_name = get_user_input(stdscr, "Input name of course to show score: ")
            for course in self.__courses: 
                if course.get_name() == course_name:
                    stdscr.addstr(f"\nList scores of students in {course.get_name()}: \n")
                    for score in self.__scores:
                        if score.get_course() == course:
                            stdscr.addstr(f"{score.get_student().get_name()}: {score.get_score()}\n")
            stdscr.addstr("=====================================================")
            stdscr.refresh()
            stdscr.getch()

    def get_course_by_name(self, course_name):
        for course in self.__courses:
            if course.get_name() == course_name:
                return course
        return None
        
    def cal_GPA(self, student_id):
        student_scores = [score.get_score() for score in self.__scores if score.get_student().get_id() == student_id]
        course_ects = [course.get_ects() for course in self.__courses]

        weighted_sum = np.dot(student_scores, course_ects)
        total_ects = np.sum(course_ects)

        return round(weighted_sum / total_ects, 1)
        
    def list_GPA(self, stdscr):
        if self.__num_students == 0 or self.__num_courses == 0:
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr("Input information for student and course first!")
            stdscr.attroff(curses.color_pair(3))
            stdscr.refresh()
            stdscr.getch()
        elif not self.__scores:
            stdscr.attron(curses.color_pair(3))
            stdscr.addstr("No score yet!")
            stdscr.attroff(curses.color_pair(3))
            stdscr.refresh()
            stdscr.getch()
        else: 
            for student in self.__students:
                gpa = self.cal_GPA(student.get_id())
                stdscr.addstr(f"{student.get_name()}: {gpa}\n")
        stdscr.refresh()
        stdscr.getch()

    def sort_student(self, stdscr):
        stdscr.addstr("Sorted student by GPA: \n")
        student_sort = sorted(self.__students, key = lambda student: self.cal_GPA(student.get_id()), reverse = True)
        for student in student_sort:
            gpa = self.cal_GPA(student.get_id())
            stdscr.addstr(f"{student.get_name()}: {gpa}\n")
        stdscr.refresh()
        stdscr.getch()

menu = ["0. Exit",
        "1. Input students' information",
        "2. Input courses' information",
        "3. Input score for specific course",
        "4. List students' information",
        "5. List courses'  information",
        "6. List score of specific course", 
        "7. List GPA",
        "8. Sort student by GPA"]

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(2))
        else:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))  

    stdscr.refresh()         


def main(stdscr):
    uni = University()

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    current_row_idx = 0
    print_menu(stdscr, current_row_idx)
    while(True):
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row_idx == 0:
                break
            elif current_row_idx == 1:
                uni.set_students(stdscr)
                stdscr.refresh()
                stdscr.getch()
            elif current_row_idx == 2:
                uni.set_courses(stdscr)
                stdscr.refresh()
                stdscr.getch() 
            elif current_row_idx == 3:
                uni.set_scores(stdscr)
                stdscr.refresh()
                stdscr.getch()
            elif current_row_idx == 4:
                uni.list_students(stdscr)
                stdscr.refresh()
                stdscr.getch()
            elif current_row_idx == 5:
                uni.list_courses(stdscr)
                stdscr.refresh()
                stdscr.getch()
            elif current_row_idx == 6:
                uni.list_scores(stdscr)
                stdscr.refresh()
                stdscr.getch()
            elif current_row_idx == 7:
                uni.list_GPA(stdscr)
                stdscr.refresh()
                stdscr.getch()
            else:
                uni.sort_student(stdscr)
                stdscr.refresh()
                stdscr.getch()
        
        print_menu(stdscr, current_row_idx)
        stdscr.refresh()

curses.wrapper(main)