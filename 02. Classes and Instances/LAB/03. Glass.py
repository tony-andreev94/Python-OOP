# https://judge.softuni.bg/Contests/Practice/Index/1936#1


class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if self.content + ml > self.capacity:
            return f"Cannot add {ml} ml"

        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        left_space = self.capacity - self.content
        return f"{left_space} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
