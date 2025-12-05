# Written by Justice V.

# A main class to test all instances for quizes

from my_duck import Duck
from my_pond import Pond
from my_student import Student
from my_course import Course
from my_lion import Lion
from my_zoo import Zoo
from my_employee import Employee
from my_department import Department

def main():

    '''
    # Students and Courses
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
    '''
    # Ducks and Ponds
    d1 = Duck("Daffy", "Black")
    d2 = Duck("Donald", "White")

    p = Pond("Front Yard Pond")

    p.add_duck(d1)
    p.add_duck(d2)

    p.ducks_quack()

    print(d1)
    print(d2)
    print(p)
    '''
    '''
    # Lions and Zoos
    l1 = Lion("Simba", "Male")
    l2 = Lion("Nala", "Female")

    z = Zoo("Minnesota Zoo")

    z.add_lion(l1)
    z.add_lion(l2)

    z.count_lions()
    z.lions_roar()
    print(z)
    '''

      # Create 2 employees
    e1 = Employee("James", "Manager")
    e2 = Employee("Alice", "Engineer")

    # Create a Department (starts with no employees)
    d = Department("IT Department", 500000)

    # Add employees
    d.add_employee(e1)
    d.add_employee(e2)

    # Show staff list
    d.show_staff_list()

    # Test is_large()
    print("Is department large?", d.is_large())

    # Show full info
    print(d)


if __name__ == "__main__":
    main()