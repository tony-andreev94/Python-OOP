# https://judge.softuni.bg/Contests/Practice/Index/1935#2


class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.set_health_to_zero()
            return f"{self.name} was defeated."

    def set_health_to_zero(self):
        # set the health to 0 if hero is defeated
        self.health = 0

    def heal(self, amount):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
