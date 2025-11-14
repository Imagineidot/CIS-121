# Written by Justice V.

class Course:
    
    def __init__(self):
        self.course_name = "Unknown"
        self.course_number = "Unknown"
        self.students = []

    def get_course_name(self):
        return self.course_name
    def set_course_name(self, course):
        self.course_name = course

    def get_course_number(self):
        return self.course_number
    def set_course_number(self, number):
        self.course_number = number

    def add_student(self, student):
        self.students.append(student.get_name())

    def show_student_enrollment(self):
        print("Students Enrolled in", self.course_name, self.course_number,": ")
        for s in self.students:
            print(" -", s)

    def __str__(self):
        return f'Course: {self.course_name} {self.course_number}, Students: {self.students}'