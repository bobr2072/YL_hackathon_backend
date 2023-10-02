from csv import DictReader

from django.core.management.base import BaseCommand
from api.models import Profit


class Command(BaseCommand):
    help = 'Загрузка данных из csv-файлов в базу данных'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Загрузка данных началась')
        )

        for row in DictReader(
            open('profit_data.csv', encoding='utf-8', mode='r'), delimiter=';', escapechar='\\'
        ):
            profit = Profit(
                id=row['id'],
                date=row['date'],
                type=row['type'],
                units=row['units'],
                units_promo=row['units_promo'],
                money=row['money'],
                money_promo=row['money_promo']
            )
            profit.save()

        self.stdout.write(
            self.style.SUCCESS('Загрузка данных завершена')
        )
