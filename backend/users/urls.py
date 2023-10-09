from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomAuthToken, UserViewSet

app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('auth/', include('djoser.urls.authtoken')),
]
