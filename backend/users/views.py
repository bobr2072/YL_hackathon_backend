from django.contrib.auth import get_user_model
from djoser.views import UserViewSet

from users.serializers import UserReadSerializer

User = get_user_model()


class UserViewSet(UserViewSet):
    """Вевьюсет пользователя."""
    queryset = User.objects.all()
    serializer_class = UserReadSerializer
