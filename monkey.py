class Monkey:
    def __init__(self, name, age, favorite_food):
        self.name = name
        self.age = age
        self.favorite_food = favorite_food

    def __str__(self):
        return f"{self.name} is {self.age} years old and loves {self.favorite_food}"
