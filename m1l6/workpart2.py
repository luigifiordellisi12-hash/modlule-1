books = ["Percy Jackson", "The Lion King", "Alice in Wonderland", "The Secret Garden", "Charlie and the Chocolate Factory"]

print(len(books))
print(books[0])
print(books[-1])
print(books[:3])
books.append("The BFG")
books.remove("The Lion King")
books.sort()
books.reverse()

librarian = {
    "name": "Mrs. Sarah",
    "section": "Science Fiction",
    "experience": 8
}

print(librarian["name"])
librarian["experience"] = 9
librarian["email"] = "sarah@schoollibrary.com"
librarian.pop("section")

book_ids = [201, 202, 203, 204, 205]
book_names = ["Percy Jackson", "Alice in Wonderland", "The Secret Garden", "Charlie and the Chocolate Factory", "The BFG"]

book_directory = dict(zip(book_ids, book_names))

print("Available Books:", books)
print("Librarian Details:", librarian)
print("Book ID Directory:", book_directory)