#!/usr/bin/env python3
# Author ID: ahscott

class Student:

    # Define the name and number when a student object is created, ex. student1 = Student('john', 025969102)
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

        # Return student name and number
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + str(self.number)

    # Add a new course and grade to students record
    def addGrade(self, course, grade):
        self.courses[course] = grade

 # Calculate the grade point average of all courses and return a string
    def displayGPA(self):
        gpa = 0.0
        for course in self.courses.keys():
            gpa = gpa + self.courses[course]
        try:    
            gpa = gpa / len(self.courses)
        except ZeroDivisionError:
            pass
        return 'GPA of student ' + self.name + ' is ' + str(gpa)