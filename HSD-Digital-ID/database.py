import sqlite3
import os

# Connect to database
connection = sqlite3.connect("students.db")
cursor = connection.cursor()
print("Successfully connected to database")

# Create table students
create_table_students = """CREATE TABLE IF NOT EXISTS students (
                            student_id INT PRIMARY KEY,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            birthdate TEXT NOT NULL,
                            course TEXT NOT NULL,
                            valid_from TEXT NOT NULL,
                            expired TEXT NOT NULL,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL);"""

cursor.execute(create_table_students)
print("Successfully created table students")

# Current path
current_path = os.path.dirname(__file__)

# Path from the text file
file_path = f"{current_path[:-14]}Datasets\\student_dataset.txt"

# Open the text file
with open(file_path, 'r') as f:
    # Processes text file 
    for line in f:
        data = line.strip().split(',')
        student_id = int(data[0])
        first_name = data[1]
        last_name = data[2]
        birthdate = data[3]
        course = data[4]
        valid_from = data[5]
        expired = data[6]

        # Insert data into table students
        cursor.execute('''INSERT OR IGNORE INTO students(student_id, first_name, last_name, birthdate, course, valid_from, expired, username, password)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (student_id, first_name, last_name, birthdate, course, valid_from, expired, username, password))
print("Successfully inserted data into database")

# save the database
connection.commit()

# close and disconnect the database
connection.close()
