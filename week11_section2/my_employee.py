# Written by Justice V.

class Employee:
    def __init__(self, name="Unknown", position="Unknown"):
        self.name = name
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def __str__(self):
        return f"Employee(name={self.name}, position={self.position})"