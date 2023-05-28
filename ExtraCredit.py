# Name: Jeana Kim
# SBUID: 115261693

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# -----------------         Search and sort fruits              -----------------
# TODO: Complete the implementation of listStatistic() and listStd().
# Declare a list of fruit in the main and run the code

def sort_fruits_alphabetically(fruits):
    """ This function sorts fruit by alphabetical order

    Args:
        fruits (list): list of fruits

    Returns:
        list: sorted list by alphabetical order
    """
    sorted_lst = sorted(fruits)
    return sorted_lst


def filter_fruits_by_length(fruits, min_length):
    """ This function filter fruits by string lenth

    Args:
        fruits (list): list of fruits
        min_length (int): minimum length for filtering

    Returns:
        list: filtered list
    """
    filtered_lst = []

    for fruit in fruits:
        length = len(fruit)
        if length >= min_length:
            filtered_lst += [fruit]
    return filtered_lst


# ---------------------------- Exercise II ---------------------------------------
# -----------------         Second-hand book E-commerce          -----------------
# TODO: Complete the implementation of searchBookTitle(),
# bubbleSortBooks() and rangeQualityCheckBooks


import csv


def read_books_from_csv(filename):
    """ This function reads the CSV file containing
    the list of Books: Title, Price, Quality, Cover

    Args:
        filename (string): relative or absolute path to the csv file

    Returns:
        list: nested list
    """
    books = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            title, price, quality, soft_cover = row
            books.append([title, float(price), int(quality), soft_cover == 'Yes'])
    return books


def searchBookTitle(list_book, title):
    """ This function  returns all the books having the name "title"
    Args:
        list_book (list): book database
        title (string): Title of the books you are looking for

    Returns:
        list: nested list
    """
    book_lst = []
    for i in range(len(list_book)):
        book_title = list_book[i][0]
        if book_title == title:
            book_lst += [list_book[i]]
    return book_lst


def shakerSortBooks(list_book, what_to_sort, ascending):
    '''
    This function sort book given one of its attribute (either price or quality)
    Args:
        list_book: book database
        what_to_sort : A string representing the field to sort by. i.e. "price" or "quality", otherwise (if any other string is entered) it will sort by price
        order : A bool representing the sort order. True for ascending order or False for descending order.
    '''
    books = []
    if what_to_sort == "quality":
        if ascending:
            w = 0
            while w < len(list_book):
                for i in range(len(list_book) - 1):
                    if list_book[i][2] > list_book[i + 1][2]:
                        list_book[i], list_book[i + 1] = list_book[i + 1], list_book[i]
                w += 1
            v = 0
            while v < len(list_book):
                for i in range(len(list_book) - 2, 0, -1):
                    if list_book[i][2] > list_book[i + 1][2]:
                        list_book[i], list_book[i + 1] = list_book[i + 1], list_book[i]
                v += 1
        else:
            w = 0
            while w < len(list_book):
                for i in range(len(list_book) - 1):
                    if list_book[i][2] < list_book[i + 1][2]:
                        list_book[i], list_book[i + 1] = list_book[i + 1], list_book[i]
                w += 1
            v = 0
            while v < len(list_book):
                for i in range(len(list_book) - 2, 0, -1):
                    if list_book[i][2] < list_book[i + 1][2]:
                        list_book[i], list_book[i + 1] = list_book[i + 1], list_book[i]
                v += 1
    else:
        if ascending:
            w = 0
            while w < len(list_book):
                for i in range(len(list_book) - 1):
                    if list_book[i][1] > list_book[i + 1][1]:
                        list_book[i], list_book[i + 1] = list_book[i + 1], list_book[i]
                w += 1
            v = 0
            while v < len(list_book):
                for i in range(len(list_book) - 2, 0, -1):
                    if list_book[i][1] > list_book[i + 1][1]:
                        list_book[i], list_book[i + 1] = list_book[i + 1], list_book[i]
                v += 1
        else:
            w = 0
            while w < len(list_book):
                for i in range(len(list_book) - 1):
                    if list_book[i][1] < list_book[i + 1][1]:
                        list_book[i], list_book[i + 1] = list_book[i + 1], list_book[i]
                w += 1
            v = 0
            while v < len(list_book):
                for i in range(len(list_book) - 2, 0, -1):
                    if list_book[i][1] < list_book[i + 1][1]:
                        list_book[i], list_book[i + 1] = list_book[i + 1], list_book[i]
                v += 1


def rangeQualityCheckBooks(list_book, quality_range):
    '''
    This function filter book within a quality range (INCLUSIVE)
    Args:
        list_book (list): book database
        quality_range (list): a list with two integer values for the beginning and end range (valid range 0-5)
    '''
    result = []
    for i in range(quality_range[0] + 1, quality_range[1]):
        result += [list_book[i]]
    return result


# ---------------------------- MAIN FCT ---------------------------------
def main():
    ########################
    ## Exercise 1 - Fruits ##
    # For the exercise 1 you have to declare a list of fruit
    # And call your functions by yourself
    fruits = ['apple', 'banana', 'orange', 'kiwi', 'strawberry', 'grape', 'mango', 'blueberry', 'pineapple',
              'watermelon']
    min_length = 6
    print(sort_fruits_alphabetically(fruits), filter_fruits_by_length(fruits, min_length))

    ########################
    ## Exercise 2 - Books ##
    books = read_books_from_csv('./Books.csv')

    # 1. Search for Harry Potter books
    title = "Harry Potter"
    book_search = searchBookTitle(books, title)
    print("We can find " + str(len(book_search)) + \
          " books called " + title + " in the database ")

    # 2. Sort your book by price using bubble sort
    shakerSortBooks(book_search, "price", True)


    # 3. return only the book with the quality in a given range
    quality_range = [3,5]
    accepted_books = rangeQualityCheckBooks(book_search, quality_range)

    # Display the books
    for book in accepted_books:
        print(book)



if __name__ == "__main__":  # do not mind this line, it is something we commonly use in python. You can google
    main()  # Here we run the main
