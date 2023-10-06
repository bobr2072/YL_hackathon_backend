from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    # Запрос на получение токена http://127.0.0.1:8000/api/auth/token/login/ с полями email и password
    path('auth/', include('djoser.urls.authtoken')),
]
