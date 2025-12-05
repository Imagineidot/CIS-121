# Written by Justice V.

class Course:
    def __init__(self, course_name="Unknown", course_number="Unknown"):
        self.course_name = course_name
        self.course_number = course_number
        self.students = []      # list starts empty

    def get_course_name(self):
        return self.course_name
    def set_course_name(self, name):
        self.course_name = name

    def get_course_number(self):
        return self.course_number
    def set_course_number(self, number):
        self.course_number = number

    def add_student(self, student):
        # student is a Student object
        self.students.append(student)

    def show_student_enrollment(self):
        print(f"Students enrolled in {self.course_name} ({self.course_number}):")
        for s in self.students:
            print(f"{s.name}")

    def __str__(self):
        names = []
        for s in self.students:
            names.append(s.name)

        return f"Course(name={self.course_name}, number={self.course_number}, students={names})"