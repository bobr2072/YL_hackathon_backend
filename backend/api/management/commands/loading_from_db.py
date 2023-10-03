from csv import DictReader

from django.core.management.base import BaseCommand

from api.models import Categories, Forecast, Profit, Sales, Stores


class Command(BaseCommand):
    help = 'Загрузка данных из csv-файлов в базу данных'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Загрузка данных началась')
        )

        for row in DictReader(
            open('./static/data/stores.csv', encoding='utf-8', mode='r')
        ):
            store = Stores(
                id=row['id'],
                store_name=row['store_name'],
                city=row['city'],
                division=row['division'],
                type_format=row['type_format'],
                loc=row['loc'],
                size=row['size'],
                is_active=row['is_active']
            )
            store.save()

        for row in DictReader(
            open('./static/data/profits.csv', encoding='utf-8', mode='r')
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

        for row in DictReader(
            open('./static/data/sales.csv', encoding='utf-8', mode='r')
        ):
            sale = Sales(
                id=row['id'],
                product_name=row['product_name'],
                store=Stores.objects.get(pk=row['store_id']),
                profit=Profit.objects.get(pk=row['profit_id'])
            )
            sale.save()

        for row in DictReader(
            open('./static/data/categories.csv', encoding='utf-8', mode='r')
        ):
            category = Categories(
                id=row['id'],
                product=Sales.objects.get(pk=row['product_id']),
                group=row['group'],
                category=row['category'],
                subcategory=row['subcategory'],
                amount=row['amount']
            )
            category.save()

        for row in DictReader(
            open('./static/data/forecasts.csv', encoding='utf-8', mode='r')
        ):
            forecast = Forecast(
                id=row['id'],
                store=Stores.objects.get(pk=row['store_id']),
                product=Sales.objects.get(pk=row['product_id']),
                forecast_date=row['forecast_date'],
                forecast=row['forecast']
            )
            forecast.save()

        self.stdout.write(
            self.style.SUCCESS('Загрузка данных завершена')
        )
