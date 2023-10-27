from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

schema_view = get_schema_view(
   openapi.Info(
      title="OnlineNotes",
      default_version='v1',
      description="This is a OnlineNotes api for recording notes",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="patience@example.com"),
      license=openapi.License(name="Your License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


# Customizing the Swagger UI to include JWT token authorization
swagger_ui_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API Description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(TokenAuthentication,),  # Add authentication
)