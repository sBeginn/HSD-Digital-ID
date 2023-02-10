import sqlite3

def test_database():
        # Connect to database
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()

        # Select a column from the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students';")
        result = cursor.fetchone()
        
        # Checks if the database was created
        assert result is not None, "Database not created"
        
