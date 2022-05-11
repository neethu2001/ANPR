from sqlite import retrieve




conn = retrieve.create_connection("sqlite/data.db")
rows = retrieve.select_all_tasks(conn)
for i in rows:
    print(i)