# # https://judge.softuni.bg/Contests/Practice/Index/1937#6
#
# class Library:
#     user_records = []
#     books_available = {}  # key: Author, value: [availble books for the author]
#     rented_books = {}  # key: username, value: {usernames: {book names: days left}}
#
#     def __init__(self):
#         pass
#
#     def add_user(self, user: User):
#         if user in self.user_records:
#             return f"User with id = {user_id} already registered in the library!"
#         self.user_records.append(user)
#
#     def remove_user(self, user: User):
#         if user not in self.user_records:
#             return f"We could not find such user to remove!"
#         self.user_records.remove(user)
#
#     def change_username(self, user_id: int, new_username: str):
#         pass
#
#
# class User:
#
#     def __init__(self, user_id: int, username: str):
#         self.user_id = user_id
#         self.username = username
#         self.books = []
#
#     def get_book(self, author: str, book_name: str, days_to_return: int, library: Library):
#         if book_name in Library.books_available[author]:
#             self.books.append(book_name)
#             Library.books_available[author].remove(book_name)
#             if self.username not in Library.rented_books.keys():
#                 Library.rented_books[self.username] = {book_name: days_to_return}
#             elif self.username in Library.rented_books.keys():
#                 Library.rented_books[self.username].extend({book_name: days_to_return})  # ????? extend/append/???
#             return f"{book_name} successfully rented for the next {days_to_return} days!"
#         else:
#             return f'The book "{book_name}" is already rented and will be available in {days_to_return provided by the user rented the book} days!'
#
#
#
# user = User(12, 'Peter')
# library = Library()
# library.add_user(user)
# print(library.add_user(user))
# library.remove_user(user)
# print(library.remove_user(user))
# library.add_user(user)
# print(library.change_username(2, 'Igor'))
# print(library.change_username(12, 'Peter'))
# print(library.change_username(12, 'George'))
#
# [print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
# library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
#                                                 'The Prisoner of Azkaban',
#                                                 'The Goblet of Fire',
#                                                 'The Order of the Phoenix',
#                                                 'The Half-Blood Prince',
#                                                 'The Deathly Hallows']})
#
# user.get_book('J.K.Rowling', 'The Deathly Hallows', 17, library)
# print(library.books_available)
# print(library.rented_books)
# print(user.books)
# print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))
# print(user.return_book('J.K.Rowling', 'The Cursed Child', library))
# user.return_book('J.K.Rowling', 'The Deathly Hallows', library)
# print(library.books_available)
# print(library.rented_books)
# print(user.books)
