# https://judge.softuni.bg/Contests/Practice/Index/1936#0


class Smartphone:

    def __init__(self, memory):
        self.memory = memory
        self.used_memory = 0
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, memory):
        if self.is_on and memory + self.used_memory <= self.memory:
            self.apps.append(app)
            self.used_memory += memory
            return f"Installing {app}"
        elif not self.is_on and self.memory >= memory:
            return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        apps_count = len(self.apps)
        memory_left = self.memory - self.used_memory
        return f"Total apps: {apps_count}. Memory left: {memory_left}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
