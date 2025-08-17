import mysql.connector
from mysql.connector import Error

try:
    # Step 1: Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",      # usually localhost
        user="root",           # your MySQL username
        password="Thelionking100%"  # your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Step 2: Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    # Step 3: Handle connection errors
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Step 4: Close cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
