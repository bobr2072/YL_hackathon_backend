import datetime

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Forecast, Categories, Stores
from api.serializers import ForecastSerializer


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
        self.product = Categories.objects.create(
            store=self.store,
            product='test product',
            group='test group',
            category='test category',
            subcategory='test subcategory',
            amount=10
        )
        self.forecast_date = datetime.date.fromisoformat('2023-09-30')
        self.forecast = '''
        {
        "2022-02-02": 424
        }
        '''

    def test_forecast(self):
        """Тест создания прогноза."""

        forecast = Forecast(
            store=self.store,
            product=self.product,
            forecast_date=self.forecast_date,
            forecast=self.forecast
        )
        forecast.save()

        saved_forecast = Forecast.objects.get(id=forecast.id)

        self.assertEqual(saved_forecast.store, self.store)
        self.assertEqual(saved_forecast.product, self.product)
        self.assertEqual(saved_forecast.forecast_date, self.forecast_date)
        self.assertEqual(saved_forecast.forecast, self.forecast)

    def test_forecast_get(self):
        """Тест get метода прогноза."""

        forecast = Forecast(
            store=self.store,
            product=self.product,
            forecast_date='2023-09-30',
            forecast=self.forecast
        )
        forecast.save()

        response = self.client.get('/api/forecast', follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_forecast_post(self):
        """Тест post метода прогноза."""

        forecast_data = {
            'store': self.store,
            'product': self.product,
            'forecast_date': self.forecast_date,
            'forecast': self.forecast,
        }

        serializer = ForecastSerializer(data=forecast_data)
        self.assertTrue(serializer.is_valid())
        forecast_json = serializer.data

        response = self.client.post('/api/forecast/', forecast_json, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Forecast.objects.filter(
            store=self.store,
            product=self.product,
            forecast_date=self.forecast_date,
            forecast=self.forecast).exists()
        )
