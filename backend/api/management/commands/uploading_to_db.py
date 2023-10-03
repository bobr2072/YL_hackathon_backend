import csv
import sqlite3 as sql

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Загрузка данных из csv-файлов в базу данных'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Загрузка данных началась')
        )
        conn = sql.connect('db.sqlite3')
        c = conn.cursor()
        c.execute("SELECT * FROM api_profit")
        with open("db_data.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow([i[0] for i in c.description])
            csv_writer.writerows(c)

        conn.close()

        self.stdout.write(
            self.style.SUCCESS('Загрузка данных завершена')
        )
