# Written by Justice V.

# A main class to test all instances for quizes

from my_student import Student
from my_course import Course

def main():

    s1 = Student()
    s1.set_name("James")
    s1.set_major("Software Engineering")

    s2 = Student()
    s2.set_name("Alice")
    s2.set_major("Chemical Engineering")

    c = Course()
    c.set_course_name("Math/Pre Calc")
    c.set_course_number("115")

    c.add_student(s1)
    c.add_student(s2)

    c.show_student_enrollment

    print(s1)

if __name__ == "__main__":
    main()  