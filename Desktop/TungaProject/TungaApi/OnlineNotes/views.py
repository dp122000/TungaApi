#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from rest_framework.authtoken.models import Token
from .models import Note
from .serializers import NoteSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == "POST":
        return Response.method(request.data)
    
    return Response("Hello, world", status = 200)

@api_view(['GET', 'POST'])
def note_list(request):
    Notes = Note.objects.all() # ORM query_set
    serialized_notes = NoteSerializer(Notes, many=True).data # Serialization of query
    return Response(serialized_notes)

class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.AllowAny]

class UserLogin(generics.CreateAPIView):    # Implementing user login logic

 class UserLogout(generics.CreateAPIView):   # Implementing user logout logic
  
  class PasswordResetEmail(generics.CreateAPIView): # Implementing password reset email logic
   
   class PasswordReset(generics.CreateAPIView): # Implementing password reset logic

 # Implementing CRUD operations for managing notes using Django Rest Framework
 # Create (POST)
    class NoteCreate(generics.CreateAPIView):
       queryset = Note.objects.all()
       serializer_class = NoteSerializer

 # Read (GET)
class NoteList(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

class NoteDetail(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

 # Update (PUT)
class NoteUpdate(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

 # Delete (DELETE)
class NoteDelete(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
