from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from .views import CategoriesViewSet, SalesViewSet, ShopsViewSet, ForecastViewSet

app_name = 'api'

router = DefaultRouter()
router.register('categories', CategoriesViewSet, basename='categories')
router.register('sales', SalesViewSet, basename='sales')
router.register('shops', ShopsViewSet, basename='shops')
router.register('forecast', ForecastViewSet, basename='forecast')

urlpatterns = [
    path('', include(router.urls)),
]
