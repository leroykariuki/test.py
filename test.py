import sys
import sqlite3

# Connect to the database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS your_table (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Add data to the table
def add_data(name, age):
    cursor.execute("INSERT INTO your_table (name, age) VALUES (?, ?)", (name, age))

# Check if command-line arguments are provided
if len(sys.argv) == 3:
    name = sys.argv[1]
    age = int(sys.argv[2])
    add_data(name, age)
else:
    print("Usage: python your_script.py <name> <age>")

# Commit changes and close the connection
conn.commit()
conn.close()
