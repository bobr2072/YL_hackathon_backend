from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer


User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    """Сериализатор создания пользователя."""
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'password')


class UserReadSerializer(UserSerializer):
    """Сериализатор просмотра профиля пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'first_name', 'last_name')
