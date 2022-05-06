max_chapters = -1
max_book = ""
user = input("Which scripture would you like to learn about? ")

with open("/Users/celestegeorge/Downloads/vs/w12/books_and_chapters.txt") as data:
    for info in data:
        info = info.strip()
        details = info.split(":")

        book = details[0]
        chapters = int(details[1])
        scripture = details[2]

        if scripture.lower() == user.lower():
            print(f"S: {scripture}, B: {book}, C: {chapters}")
            if chapters > max_chapters:
                max_chapters = chapters
                max_book = book
print(f"The book with the most chapters in the {user} is: {max_book}")
print(f"It has {max_chapters} chapters.")