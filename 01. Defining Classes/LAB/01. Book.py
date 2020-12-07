# https://judge.softuni.bg/Contests/Practice/Index/1934#0
from dataclasses import dataclass


class Book:

    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


@dataclass
class Book2:
    name = str
    author = str
    pages = int


first_book = Book('Python-Basics', 'Nakov', 200)
print(first_book.name)
print(first_book.author)
print(first_book.pages)


book = Book2("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
