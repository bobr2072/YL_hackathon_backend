import sqlite3 as sql
import os
import csv

# нужен путь до базы
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite3")
conn = sql.connect(db_path)
c = conn.cursor()
c.execute("SELECT * FROM sales_profit")
with open("employee_data.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in c.description])
    csv_writer.writerows(c)

dirpath = os.getcwd() + "/employee_data.csv"
conn.close()
