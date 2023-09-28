from django.urls import admin, hello_world
from django.urls import path
from .views import views, NoteCreate
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('password_reset_email/', views.PasswordResetEmail.as_view(), name='password_reset_email'),
    path('password_reset/<str:token>/', views.PasswordReset.as_view(), name='password_reset'),
    path('api/notes/create/', NoteCreate.as_view(), name='note-create'),
    path('api/notes/', NoteList.as_view(), name='note-list'),
    path('api/notes/<int:pk>/', NoteDetail.as_view(), name='note-detail'),
    path('api/notes/<int:pk>/update/', NoteUpdate.as_view(), name='note-update'),
    path('api/notes/<int:pk>/delete/', NoteDelete.as_view(), name='note-delete'),
   
]

