# https://judge.softuni.bg/Contests/Practice/Index/1934#1

x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
        return x

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    return change_global()


print(x)
outer()
print(x)
