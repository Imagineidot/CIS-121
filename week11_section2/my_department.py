# Written by Justice V.

class Department:
    def __init__(self, dept_name="Unknown", budget=0):
        self.dept_name = dept_name
        self.budget = budget
        self.employees = []      # must start empty

    def get_budget(self):
        return self.budget
    def set_budget(self, budget):
        self.budget = budget
        
    def add_employee(self, employee):
        # employee is an Employee object
        self.employees.append(employee)

    def show_staff_list(self):
        print(f"Employees in {self.dept_name}:")
        for emp in self.employees:
            print(f"{emp.name}, {emp.position}")

    def is_large(self):
        # large if 10 or more employees
        return len(self.employees) >= 10

    def __str__(self):
        names = []
        for emp in self.employees:
            names.append(emp.name)
        return f"Department(name={self.dept_name}, budget={self.budget}, employees={names})"