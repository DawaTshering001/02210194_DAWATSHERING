import json
import os

FILE_NAME = "books.json"

# ---------- Helper functions ----------
def load_books():
    """Load books from JSON file"""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
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
        print(f" Book ID {book_id} not found!")
    else:
        save_books(new_books)
        print(f" Book ID {book_id} deleted successfully!")


# ---------- Example Usage ----------
def menu():
    while True:
        print("\n📚 Book Management Menu")
        print("1. View Books")
        print("2. Add Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            read_books()
        elif choice == "2":
            try:
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")
                year = int(input("Enter Year: "))
                add_book({"id": book_id, "title": title, "author": author, "year": year})
            except ValueError:
                print("⚠️ Invalid input! Please enter numbers for ID and Year.")
        elif choice == "3":
            try:
                book_id = int(input("Enter Book ID to update: "))
                title = input("Enter new Title (leave blank to keep same): ")
                author = input("Enter new Author (leave blank to keep same): ")
                year_input = input("Enter new Year (leave blank to keep same): ")
                new_data = {}
                if title: new_data["title"] = title
                if author: new_data["author"] = author
                if year_input: new_data["year"] = int(year_input)
                update_book(book_id, new_data)
            except ValueError:
                print("⚠️ Invalid input for ID or Year!")
        elif choice == "4":
            try:
                book_id = int(input("Enter Book ID to delete: "))
                delete_book(book_id)
            except ValueError:
                print("⚠️ Invalid input! Book ID must be a number.")
        elif choice == "5":
            print("👋 Exiting Book Management System. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please select 1-5.")


# ---------- Run Program ----------
if __name__ == "__main__":
    menu()