# https://judge.softuni.bg/Contests/Practice/Index/1934#4


class Flower:
    is_happy = False

    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if not self.is_happy:
            return f"{self.name} is not happy"
        else:
            return f"{self.name} is happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())
