import sqlite3

try:
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    print("Successfully Connected to SQLite")

    cursor.execute("""CREATE TABLE IF NOT EXISTS VEHICLES(
    NUMBER TEXT PRIMARY KEY,
   DATE DATE,
   TIME TIME);
    """)
    conn.commit()
    print("SQLite script executed successfully")
    cursor.close()

except sqlite3.Error as error:
    print("Error while executing sqlite script", error)
finally:
    if conn:
        conn.close()
        print("sqlite connection is closed")