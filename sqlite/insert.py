import sqlite3
from datetime import date
try:
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    print("Connected to SQLite")

    # sqlite_insert_query = """INSERT INTO VEHICLES
                        #   (NUMBER,DATE,TIME) 
                        #   VALUES ("KL31M4154","10-06-2021","04:26:25");"""
    sqlite_insert_query =       """INSERT INTO VEHICLES
                          (NUMBER,DATE,TIME) 
                          VALUES (?, ?, ?)",(name,));"""
    cursor.execute(sqlite_insert_query)


    conn.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Error while working with SQLite", error)
finally:
    if conn:
        print("Total Rows affected since the database connection was opened: ", conn.total_changes)
        conn.close()
        print("sqlite connection is closed")