from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from api.swagger import schema_view
from api.views import (CategoriesViewSet, ForecastViewSet, SalesViewSet,
                       StoresViewSet)

app_name = 'api'

router = DefaultRouter()
router.register('categories', CategoriesViewSet, basename='categories')
router.register('sales', SalesViewSet, basename='sales')
router.register('shops', StoresViewSet, basename='shops')
router.register('forecast', ForecastViewSet, basename='forecast')

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.as_view(), name='schema-json'),
]
