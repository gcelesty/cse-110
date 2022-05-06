with open("/Users/celestegeorge/Downloads/vs/w11/books.txt") as bom:
    for book in bom:
        book = book.strip()
        print(book)
