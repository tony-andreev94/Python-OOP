# # https://judge.softuni.bg/Contests/Practice/Index/2430#2

class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for each in args:
            result *= each
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for each in args[1:]:
            result /= each
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for each in args[1:]:
            result -= each
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 10, 10))
print(Calculator.subtract(15, 5, 5))
print(Calculator.divide(100, 10, 5))

print()

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))