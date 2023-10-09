from csv import DictReader

from django.core.management.base import BaseCommand

from api.models import (Profit, Stores, Categories,
                        Product, Sales, Forecast)


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

        for row in DictReader(
            open('stores_data.csv', encoding='utf-8', mode='r'), delimiter=';', escapechar='\\'
        ):
            store = Stores(
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
            open('categories_data.csv', encoding='utf-8', mode='r'), delimiter=';', escapechar='\\'
        ):
            category = Categories(
                id=row['id'],
                product=Product.objects.get(pk=row['product_id']),
                store=Stores.objects.get(pk=row['store_id']),
                group=row['group'],
                category=row['category'],
                subcategory=row['subcategory'],
                amount=row['amount']
            )
            category.save()

        for row in DictReader(
            open('products_data.csv', encoding='utf-8', mode='r'), delimiter=';', escapechar='\\'
        ):
            product = Product(
                id=row['id'],
                name=row['name']
            )
            product.save()

        for row in DictReader(
            open('sales_data.csv', encoding='utf-8', mode='r'), delimiter=';', escapechar='\\'
        ):
            sale = Sales(
                id=row['id'],
                product=Product.objects.get(pk=row['product_id']),
                store=Stores.objects.get(pk=row['store_id']),
                profit=Profit.objects.get(pk=row['profit_id'])
            )
            sale.save()

        for row in DictReader(
            open('forecasts_data.csv', encoding='utf-8', mode='r'), delimiter=';', escapechar='\\'
        ):
            forecast = Forecast(
                id=row['id'],
                product=Product.objects.get(pk=row['product_id']),
                store=Stores.objects.get(pk=row['store_id']),
                forecast_date=row['forecast_date'],
                forecast=row['forecast']
            )
            forecast.save()

        self.stdout.write(
            self.style.SUCCESS('Загрузка данных завершена')
        )
