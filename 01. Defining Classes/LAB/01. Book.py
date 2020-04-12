# https://judge.softuni.bg/Contests/Practice/Index/1934#0

class Book:

    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


first_book = Book('Python-Basics', 'Nakov', 200)
print(first_book.name)
print(first_book.author)
print(first_book.pages)