from django.contrib.auth import get_user_model
from djoser.views import UserViewSet

from users.serializers import UserReadSerializer

User = get_user_model()


class UserViewSet(UserViewSet):
    """Вььюсет пользователя."""

    queryset = User.objects.all()
    serializer_class = UserReadSerializer
