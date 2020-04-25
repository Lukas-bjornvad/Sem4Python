import random
import csv
import matplotlib.pyplot as plt
import numpy as np



class Student():
    def __init__(self, name, gender, datasheet, imageurl):
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
        self.imageurl = imageurl

    def get_avg_grade(self):
        grad = self.datasheet.get_grades_as_list()
        sum = 0
        for obj in grad:
            sum += int(obj)
        average = sum/len(grad)
        return average

    def completed_courses(self):
        completed = int(self.datasheet.passedECTS())
        return ((completed/150)*100)

    def get_courses(self):
        return self.datasheet.get_courses()


class DataSheet():
    def __init__(self, courses=[]):
        self.courses = courses

    def add_course(self, course):
        self.courses.append(course)

    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            grades.append(course.grade)
        return grades

    def passedECTS(self):
        ec = 0
        for course in self.courses:
            if int(course.grade) >= 2:
                ec += int(course.ECTS)
        return ec

    def get_courses(self):
        return self.courses


class Course():
    def __init__(self, name, classroom, teacher, ECTS, grade: int = None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade


