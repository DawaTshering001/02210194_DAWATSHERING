import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

print("=== Book List ===")
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    print(f"Title: {title}, Author: {author}")
for book in root.findall('book'):
    title = book.find('title').text
    if title == "1984":
        book.find('price').text = "11.99"

tree.write('books.xml')  # Save the changes
print("✅ Price updated.")
for book in root.findall('book'):
    title = book.find('title').text
    if title == "Clean Code":
        root.remove(book)

tree.write('books.xml')  # Save the updated file
print("❌ Book deleted.")
