# Written by Justice V.

class Duck:
    def __init__(self, name="Unknown", color="Unknown"):
        self.name = name
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def speak(self):
        print("Quack!")

    def __str__(self):
        return f"Duck(name={self.name}, color={self.color})"
