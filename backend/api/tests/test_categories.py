from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Categories, Product, Stores


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
        self.product = Product.objects.create(name='test product')
        self.group = 'test group'
        self.category = 'test category'
        self.subcategory = 'test subcategory'

    def test_categories(self):
        """Тест создания категорий."""

        category = Categories(
            store=self.store,
            product=self.product,
            group=self.group,
            category=self.category,
            subcategory=self.subcategory,
            amount=10
        )
        category.save()

        saved_category = Categories.objects.get(product=category.product)

        self.assertEqual(saved_category.product, self.product)
        self.assertEqual(saved_category.group, self.group)
        self.assertEqual(saved_category.category, self.category)
        self.assertEqual(saved_category.subcategory, self.subcategory)
        self.assertEqual(saved_category.amount, 10)

    def test_categories_get(self):
        """Тест get метода категорий."""

        category = Categories(
            store=self.store,
            product=self.product,
            group=self.group,
            category=self.category,
            subcategory=self.subcategory,
            amount=10
        )
        category.save()

        response = self.client.get('/api/categories', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
