from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Profit, Sales, Stores, Categories


class SalesModelTestCase(TestCase):

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
        self.product_name = Categories.objects.create(
            store=self.store,
            product='test product',
            group='test group',
            category='test category',
            subcategory='test subcategory',
            amount=10
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
        """Тест создания продаж товаров."""

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
        """Тест get метода продаж товаров."""

        sales = Sales(
            product_name=self.product_name,
            store=self.store
        )
        sales.save()

        sales.profit.set([self.profit])

        response = self.client.get('/api/sales', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
