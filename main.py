from books import show_books

name = input("What's your name? ")
print("Welcome", name)

books = []
number = int(input("How many books do you want to add? : "))

for i in range(number):
    book = input("Enter the name of the book: ")
    books.append(book)


show_books(books)
