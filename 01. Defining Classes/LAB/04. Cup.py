# https://judge.softuni.bg/Contests/Practice/Index/1934#3


class Cup:

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    # initial example
    def fill(self, milliliters):
        if milliliters + self.quantity <= self.size:
            # run code/ do something
            self.quantity += milliliters

    # defensive programming example
    def fill_defensive(self, milliliters):
        # check all invalid cases:
        if milliliters + self.quantity > self.size:
            return
        # run code
        self.quantity += milliliters

    def status(self):
        return self.size - self.quantity


class Cup2:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def check_capacity(self, milliliters):
        if milliliters <= self.size - self.quantity:
            return True
        else:
            return False

    def fill(self, milliliters):
        if self.check_capacity(milliliters):
            self.quantity += milliliters

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
