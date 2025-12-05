# Written by Justice V.

class Zoo:
    def __init__(self, location = "Unknown"):
        self.location = location
        self.lions = []

    def add_lion(self, lion):
        self.lions.append(lion)

    def lions_roar(self):
        for lion in self.lions:
            print(f"{lion.name}: ", end="")
            lion.roar()
    
    def count_lions(self):
        male_count = 0
        female_count = 0

        for lion in self.lions:
            if lion.gender.lower() == "male":
                male_count += 1
            elif lion.gender.lower() == "female":
                female_count += 1
        
        print(f'Males: {male_count}, Females: {female_count}')

    def __str__(self):
        names = []
        for lion in self.lions:
            names.append(lion.name)

        return f'Zoo(Location: {self.location}, lions: {names})'