# < Name >
# < SBU Email Address >

# Create your library class here
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __repr__(self):
        temp = ""
        for book in self.books:
            temp += book
            temp += " "
        return self.name + ": " + temp

    def addBook(self, bookTitle):
        self.books.append(bookTitle)


# Do not modify the test cases below
a = Library("Local Library")
a.addBook("'Sunny Day'")
a.addBook("'Brown Fox'")

print(a) # should print:  Local Library: 'Sunny Day' 'Brown Fox'