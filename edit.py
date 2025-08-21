import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('BOOKS.xml')
root = tree.getroot()

# Display all books
print("=== 📚 Book List ===")
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    print(f"Title: {title}, Author: {author}")

# 🔁 Update price of book titled "1984"
for book in root.findall('book'):
    title = book.find('title').text
    if title == "1984":
        book.find('price').text = "299"
        print("✅ Updated price for '1984' to 299.")

# 🗑️ Delete the book titled "Clean Code"
for book in root.findall('book'):
    title = book.find('title').text
    if title == "Clean Code":
        root.remove(book)
        print("❌ Deleted book titled 'Clean Code'.")

# 💾 Save the changes back to the XML file
tree.write('BOOKS.xml')
print("✅ Changes saved to books.xml.")
