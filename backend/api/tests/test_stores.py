from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Stores


class StoresModelTestCase(TestCase):

    def setUp(self):

        self.client = APIClient()
        self.store_name = 'test store'
        self.city = 'test city'
        self.division = 'test division'

    def test_stores(self):
        """Тест создания магазинов."""

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

        saved_store = Stores.objects.get(store_name=store.store_name)

        self.assertEqual(saved_store.store_name, self.store_name)
        self.assertEqual(saved_store.city, self.city)
        self.assertEqual(saved_store.division, 'test division')
        self.assertEqual(saved_store.type_format, 1)
        self.assertEqual(saved_store.loc, 1)
        self.assertEqual(saved_store.size, 10)
        self.assertTrue(saved_store.is_active)

    def test_stores_get(self):
        """Тест get метода магазина."""

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

        response = self.client.get('/api/shops', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
