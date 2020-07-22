# https://judge.softuni.bg/Contests/Practice/Index/1934#0


def generate_row(index, n):
    indent = ' ' * (n - index - 1)
    stars = '* ' * (index + 1)
    return f"{indent}{stars}"


def print_rhombus(n):
    for i in range(n):
        print(generate_row(i, n))

    for i in range(n - 2, -1, -1):
        print(generate_row(i, n))


print_rhombus(int(input()))
