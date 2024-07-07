import threading
import sqlite3


# Function to perform database operations
def perform_database_operations():
    try:
        # Connect to the database
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()

        # Create a table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                         (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

        # Insert some data
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Charlie', 35))

        # Commit changes and close connection
        connection.commit()
        connection.close()
        print("Database operations successful")
    except Exception as e:
        print("Error performing database operations:", e)


# Function to perform multithreading
def perform_multithreading():
    try:
        # Create threads
        thread1 = threading.Thread(target=perform_database_operations)
        thread2 = threading.Thread(target=perform_database_operations)

        # Start threads
        thread1.start()
        thread2.start()

        # Join threads to wait for completion
        thread1.join()
        thread2.join()
        print("Multithreading successful")
    except Exception as e:
        print("Error performing multithreading:", e)


# Main function
if __name__ == "__main__":
    perform_multithreading()
