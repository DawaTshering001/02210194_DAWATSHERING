import json
import os

FILE_NAME = "books.json"

 
    # ---------- Helper functions ----------
def load_books():
    if not os.path.exists(FILE_NAME):
        return[]
    with open(FILE_NAME,"r") as file: 
        return json.load(file)

def save_books(books):
    """Save books to JSON file"""
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


# ---------- CRUD Operations ----------
def add_book(book):
    books = load_books()
    books.append(book)
    save_books(books)
    print(f"✅ Book '{book['title']}' added successfully!")

def read_books():
    books = load_books()
    if not books:
        print("📂 No books found.")
        return
    for book in books:
        print(f"ID: {book['id']} | {book['title']} by {book['author']} ({book['year']})")

def update_book(book_id, new_data):
    books = load_books()
    for book in books:
        if book["id"] == book_id:
            book.update(new_data)
            save_books(books)
            print(f"✏️ Book ID {book_id} updated successfully!")
            return
    print(f"⚠️ Book ID {book_id} not found!")

def delete_book(book_id):
    books = load_books()
    new_books = [book for book in books if book["id"] != book_id]
    if len(books) == len(new_books):
        print(f"⚠️ Book ID {book_id} not found!")
    else:
        save_books(new_books)
        print(f"🗑️ Book ID {book_id} deleted successfully!")


# ---------- Example Usage ----------
if __name__ == "__main__":
    # Add new book
    add_book({"id": 3, "title": "Machine Learning", "author": "Andrew Ng", "year": 2019})

    # Read all books
    print("\n📚 All Books:")
    read_books()

    # Update a book
    update_book(2, {"title": "Advanced Data Science", "year": 2022})

    # Delete a book
    delete_book(1)

    # Final list
    print("\n📚 Final Books:")
    read_books()
