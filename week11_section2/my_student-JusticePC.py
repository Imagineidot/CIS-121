# Written by Justice V.

class Student: 
    
    def __init__(self):
        self.name = "Unknown"
        self.major = "Unknown"
    
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_major(self):
        return self.major
    def set_major(self, major):
        self.major = major

    def __str__(self):
        return f'Name: {self.name}, Major: {self.major}'
        