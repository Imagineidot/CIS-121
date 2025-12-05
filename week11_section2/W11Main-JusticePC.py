# Written by Justice V.

# A main class to test all instances for quizes

from my_duck import Duck
from my_pond import Pond
from my_student import Student
from my_course import Course



def main():

    '''
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

    print(c)
    '''

    d1 = Duck()
    d1.set_name("Donald")
    d1.set_color("White")

    d2 = Duck()
    d2.set_name("Daisy")
    d2.set_color("White")

    p = Pond()
    p.set_name("Quackxia")
    p.add_duck(d1)
    p.add_duck(d2)

    p.ducks_quack
    print(p)


if __name__ == "__main__":
    main()  