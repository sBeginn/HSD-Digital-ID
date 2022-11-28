import sqlite3


    
#Verbindung zur Datenbank
connection = sqlite3.connect("students.db")
cursor = connection.cursor()
print("Successfully connected to database")


#Erstellt Tabelle Studenten

create_table_students = """CREATE TABLE IF NOT EXISTS students (
                            student_id INT PRIMARY KEY,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            birthdate TEXT NOT NULL,
                            course TEXT NOT NULL,
                            valid_from TEXT NOT NULL,
                            expired TEXT NOT NULL);"""

cursor.execute(create_table_students)
print("Successfully created table students")


#Inhalt Tabelle Studenten

input_table_students = """INSERT OR IGNORE INTO students(student_id, first_name, last_name, birthdate, course, valid_from, expired)
                            VALUES 
                            (?, ?, ?, ?, ?, ?, ?);"""
      
input_data = [(1, 'a', 'b', '01.01.2000', 'daisy', '01.01.2020', '01.01.2021')]
        
cursor.executemany(input_table_students, input_data) 
print("Successfully inserted data into database")


connection.commit()
connection.close()
