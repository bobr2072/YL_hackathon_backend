from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoriesViewSet, ForecastViewSet, SalesViewSet,
                       StoresViewSet)

app_name = 'api'

router = DefaultRouter()
router.register('categories', CategoriesViewSet, basename='categories')
router.register('sales', SalesViewSet, basename='sales')
router.register('shops', StoresViewSet, basename='shops')
router.register('forecast', ForecastViewSet, basename='forecast')

urlpatterns = [
    path('v0/', include(router.urls)),
]
