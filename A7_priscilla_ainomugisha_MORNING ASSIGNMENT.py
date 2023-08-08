#ASSIGNMENT
## Show a context manager for file handling that automatically opens and closes a file.
with open('bsse.txt', 'a') as f:
    message = 'Welcome to BSSE'
    f.write(message)
    
    

## show a context manager for managing a database connection using the contextlib module:
import contextlib
import mysql.connector

@contextlib.contextmanager
def database_connection(host, port, username, password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=database
        )
        yield connection
    finally:
        if connection:
            connection.close()

with database_connection(host='localhost', port='3306', username='priscilla', password='Root@123', database='star_db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM regNo')
    result = cursor.fetchall()
    for row in result:
        print(row)

## Show an example that demonstrates multithreading and multiprocessing in Python to run a function for different amounts of time:
import threading
import multiprocessing
import time

def set_alarm(duration):
    print(f"Setting my alarm for {duration} seconds")
    time.sleep(duration)
    print(f"Finished setting my alarm for {duration} seconds")

# Multithreading
thread1 = threading.Thread(target=set_alarm, args=(2,))
thread2 = threading.Thread(target=set_alarm, args=(4,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Multiprocessing
process1 = multiprocessing.Process(target=set_alarm, args=(2,))
process2 = multiprocessing.Process(target=set_alarm, args=(4,))

process1.start()
process2.start()

process1.join()
process2.join()