import os
import gzip
import numpy as np
import curses
from domains import *
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
        self.decompress_file()

    def __del__(self):
        self.compress_file()

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
        with open("student.txt", "w") as student_file:
            student_file.write(f"{str('ID').ljust(8)}\t{str('Name').ljust(8)}\t{str('DOB').ljust(8)}\n")
            for _ in range (num_students):
                id = get_user_input(stdscr, "Input ID of student: ")
                stdscr.refresh()
                name = get_user_input(stdscr, "Input name of student: ")
                stdscr.refresh()
                dob = get_user_input(stdscr, "Input day of birth of student: ")
                stdscr.refresh()
                student = Student(id, name, dob)
                self.__students.append(student)
                student_file.write(f"{str(id).ljust(8)}\t{str(name).ljust(8)}\t{str(dob).ljust(8)}\n")

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
        with open("course.txt", "w") as course_file:
            course_file.write(f"{str('ID').ljust(8)}\t{str('Course Name').ljust(8)}\t{str('ECTS').ljust(8)}\n")
            for _ in range (num_courses):
                id = get_user_input(stdscr, "Input ID of course: ")
                stdscr.refresh()
                name = get_user_input(stdscr, "Input name of course: ")
                stdscr.refresh()
                ects = int(get_user_input(stdscr, "Input ects for course: "))
                stdscr.refresh()
                course = Course(id, name, ects)
                self.__courses.append(course)  
                course_file.write(f"{str(id).ljust(8)}\t{str(name).ljust(8)}\t{str(ects).ljust(8)}\n")
            
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
        with open("score.txt", "w") as score_file:
            score_file.write(f"{str('Student ID').ljust(8)}\t{str('Student').ljust(8)}\t{str('Course').ljust(8)}\t{str('Score').ljust(8)}\n")
            for student in self.__students:
                score = float(get_user_input(stdscr, f"Input score for {student.get_name()} in {course_name}: "))
                stdscr.refresh()
                stdscr.getch()
                student_score = Score(course, student, score)
                self.__scores.append(student_score)
                score_file.write(f"{str(student_score.get_student().get_id()).ljust(8)}\t{str(student_score.get_student().get_name()).ljust(8)}\t{str(student_score.get_course().get_name()).ljust(8)}\t{str(student_score.get_score()).ljust(8)}\n")


    def get_students(self):
        return self.__students
    
    def get_courses(self):
        return self.__courses
    
    def get_num_students(self):
        return self.__num_students
    
    def get_num_courses(self):
        return self.__num_courses
    
    def compress_file(self):
        try:
            with open("student.txt", "r") as student_file:
                student_data = student_file.read().encode("utf-8")
            with open("course.txt", "r") as course_file:
                course_data = course_file.read().encode("utf-8")
            with open("score.txt", "r") as score_file:
                score_data = score_file.read().encode("utf-8")
            
            compressed_data = gzip.compress(student_data  + course_data + score_data)

            with gzip.open("students.dat", "ab") as compressed_file:
                compressed_file.write(compressed_data)
        except IOError:
            print(f"Error compressing files: {IOError}")

    def decompress_file(self):
        if os.path.exists("students.dat"):
            try:
                with gzip.open("students.dat", "rb") as compressed_file:
                    compressed_data = compressed_file.read()
                    decompressed_data = gzip.decompress(compressed_data)

                with open("decompressed.dat", "wb") as decompressed_file:
                    decompressed_file.write(decompressed_data)
            except IOError:
                print(f"Error decompressing files: {IOError}")
    
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