from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from users.serializers import UserReadSerializer

User = get_user_model()


class UserViewSet(UserViewSet):
    """Вььюсет пользователя."""

    queryset = User.objects.all()
    serializer_class = UserReadSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email,
            'position': user.position
        })
