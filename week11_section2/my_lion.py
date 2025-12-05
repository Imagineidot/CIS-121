# Written by Justice V.

class Lion:
    def __init__(self, name = "Unknown", gender = "Unknown"):
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = "Unknown"

    def roar(self):
        print("Roar!")

    def __str__(self):
        return f'Lion(Name: {self.name}, Gender: {self.gender})'