import sqlite3
class insert:


    def connect_insert(db,vehicle_id,date,time):
            try:
                conn = sqlite3.connect(db)
                cursor = conn.cursor()
                print("Connected to SQLite")
                cursor.execute("INSERT INTO VEHICLES VALUES (?, ?, ?);", (vehicle_id,date,time))


                conn.commit()
                cursor.close()

            except sqlite3.Error as error:
                print("Error while working with SQLite", error)
            finally:
                if conn:
                    print("Total Rows affected since the database connection was opened: ", conn.total_changes)
                    conn.close()
                    print("sqlite connection is closed")



