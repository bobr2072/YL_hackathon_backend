from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API for hackathon team 10/10",
        default_version='v0',
        description="API documentation for backend",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
