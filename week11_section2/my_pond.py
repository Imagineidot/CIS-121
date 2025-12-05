# Written by Justice V.

class Pond:
    def __init__(self, name="Unknown"):
        self.name = name
        self.ducks = []   # start with no ducks

    def add_duck(self, duck):
        self.ducks.append(duck)

    def ducks_quack(self):
        print(f"Ducks in pond '{self.name}' are quacking:")
        for duck in self.ducks:
            print(f"{duck.name}: ", end="")
            duck.speak()

    def __str__(self):
        names = []
        for duck in self.ducks:
            names.append(duck.name)

        return f"Pond(name={self.name}, ducks={names})"