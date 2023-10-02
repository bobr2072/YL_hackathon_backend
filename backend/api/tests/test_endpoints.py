import datetime

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Categories, Forecast, Profit, Sales, Stores


class CategoriesModelTestCase(TestCase):

    def setUp(self):

        self.client = APIClient()
        self.store = Stores.objects.create(
            store_name='test store',
            city='test city',
            division='test division',
            type_format=1,
            loc=12345,
            size=1000,
            is_active=True
        )
        self.product = Sales.objects.create(
            product_name='test product',
            store=self.store,
        )
        self.group = 'test group'
        self.category = 'test category'
        self.subcategory = 'test subcategory'

    def test_categories(self):

        category = Categories(
            product=self.product,
            group=self.group,
            category=self.category,
            subcategory=self.subcategory,
            amount=10
        )
        category.save()

        saved_category = Categories.objects.get(id=category.id)

        self.assertEqual(saved_category.product, self.product)
        self.assertEqual(saved_category.group, self.group)
        self.assertEqual(saved_category.category, self.category)
        self.assertEqual(saved_category.subcategory, self.subcategory)
        self.assertEqual(saved_category.amount, 10)

    def test_categories_get(self):

        category = Categories(
            product=self.product,
            group=self.group,
            category=self.category,
            subcategory=self.subcategory,
            amount=10
        )
        category.save()

        response = self.client.get('/api/v0/categories', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class SalesModelTestCase(TestCase):

    def setUp(self):

        self.client = APIClient()
        self.product_name = 'test product'
        self.store = Stores.objects.create(
            store_name='test store',
            city='test city',
            division='test division',
            type_format=1,
            loc=12345,
            size=1000,
            is_active=True
        )
        self.profit = Profit.objects.create(
            date='2023-09-30',
            type=True,
            units=10,
            units_promo=5,
            money=100.0,
            money_promo=50.0
        )

    def test_sales(self):

        sales = Sales(
            product_name=self.product_name,
            store=self.store,
        )
        sales.save()

        sales.profit.set([self.profit])

        saved_sales = Sales.objects.get(id=sales.id)

        self.assertEqual(saved_sales.product_name, self.product_name)
        self.assertEqual(saved_sales.store, self.store)

        self.assertEqual(saved_sales.profit.count(), 1)
        self.assertEqual(saved_sales.profit.first(), self.profit)

    def test_sales_get(self):

        sales = Sales(
            product_name=self.product_name,
            store=self.store
        )
        sales.save()

        sales.profit.set([self.profit])

        response = self.client.get('/api/v0/sales', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class StoresModelTestCase(TestCase):

    def setUp(self):

        self.client = APIClient()
        self.store_name = 'test store'
        self.city = 'test city'
        self.division = 'test division'

    def test_stores(self):

        store = Stores(
            store_name=self.store_name,
            city=self.city,
            division=self.division,
            type_format=1,
            loc=1,
            size=10,
            is_active=True
        )
        store.save()

        saved_store = Stores.objects.get(id=store.id)

        self.assertEqual(saved_store.store_name, self.store_name)
        self.assertEqual(saved_store.city, self.city)
        self.assertEqual(saved_store.division, 'test division')
        self.assertEqual(saved_store.type_format, 1)
        self.assertEqual(saved_store.loc, 1)
        self.assertEqual(saved_store.size, 10)
        self.assertTrue(saved_store.is_active)

    def test_stores_get(self):

        store = Stores(
            store_name=self.store_name,
            city=self.city,
            division=self.division,
            type_format=1,
            loc=12345,
            size=1000,
            is_active=True
        )
        store.save()

        response = self.client.get('/api/v0/shops', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ForecastModelTestCase(TestCase):

    def setUp(self):

        self.client = APIClient()
        self.store = Stores.objects.create(
            store_name='test store',
            city='test city',
            division='test division',
            type_format=1,
            loc=1,
            size=10,
            is_active=True
        )
        self.product = Sales.objects.create(
            product_name='test product',
            store=self.store,
        )
        self.forecast_date = '2023-09-30'
        self.forecast = '''
        {
        "2022-02-02": 424
        }
        '''

    def test_forecast(self):
        forecast_date = datetime.date.fromisoformat(self.forecast_date)

        forecast = Forecast(
            store=self.store,
            product=self.product,
            forecast_date=forecast_date,
            forecast=self.forecast
        )
        forecast.save()

        saved_forecast = Forecast.objects.get(id=forecast.id)

        self.assertEqual(saved_forecast.store, self.store)
        self.assertEqual(saved_forecast.product, self.product)
        self.assertEqual(saved_forecast.forecast_date, forecast_date)
        self.assertEqual(saved_forecast.forecast, self.forecast)

    def test_forecast_get(self):

        forecast = Forecast(
            store=self.store,
            product=self.product,
            forecast_date='2023-09-30',
            forecast=self.forecast
        )
        forecast.save()

        response = self.client.get('/api/v0/forecast', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
