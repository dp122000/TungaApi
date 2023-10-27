"""
URL configuration for TungaApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from OnlineNotes.views import hello_world  #OnlineNotes.urls
from django.urls import path, re_path, include
from OnlineNotes.views import *
from OnlineNotes import views 
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Online Notes API",
        default_version='v1',
        description="API for Online Notes Application",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="patience@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('OnlineNotes.urls')), 
    path('hello/', hello_world),
    path('api/register/', views.UserRegister.as_view(), name='register'),
    path('api/login/', views.UserLogin.as_view(), name='login'),
    path('api/logout/', views.UserLogout.as_view(), name='logout'),
    path('password_reset_email/', views.PasswordResetEmail.as_view(), name='password_reset_email'),
    path('password_reset/<str:token>/', views.PasswordReset.as_view(), name='password_reset'),
    path('api/notes/create/', NoteCreateView.as_view(), name='note-create'),
    path('api/notes/', NoteListView.as_view(), name='note-list'),
    path('api/notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('api/notes/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('api/notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
