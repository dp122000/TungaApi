#from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import generics, permissions, status, filters
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import viewsets
#from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#from rest_framework.authtoken.models import Token
from .models import Note, Category
from .serializers import CategorySerializer, NoteSerializer
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.core.mail import send_mail
import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == "POST":
        return Response.method(request.data)
    
    return Response("Hello, world", status = 200)

class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.AllowAny]

class UserLogin(generics.CreateAPIView):    # Implementing user login logic
    serializer_class = NoteSerializer
    pass  # Placeholder when the class is empty

class UserLogout(generics.CreateAPIView):   # Implementing user logout logic
    serializer_class = NoteSerializer
    pass  # Placeholder when the class is empty
  
class PasswordResetEmail(generics.CreateAPIView): # Implementing password reset email logic
    serializer_class = NoteSerializer
    pass  # Placeholder when the class is empty
   
class PasswordReset(generics.CreateAPIView): # Implementing password reset logic
    serializer_class = NoteSerializer
    pass  # Placeholder when the class is empty

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    action = {'get': 'list', 'post': 'create'}

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    action = {'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Implementing CRUD operations for managing notes using Django Rest Framework
# Create (POST)
class NoteCreateView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        # Create a serializer instance with the provided data
     serializer = self.get_serializer(data=request.data)

        # Check if the data is valid
     if serializer.is_valid():
            # If valid, save the data
        self.perform_create(serializer)
        return Response({
            'status': 'success',
            'message': 'Note created successfully.',
            'data': serializer.data
         }, status=status.HTTP_201_CREATED)
     else:
            # If validation fails, provide feedback
        return Response({
             'status': 'error',
                'message': 'Validation failed',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
# If the data is valid, a success response is returned with a status code of 201 (created).
# If the data does not pass validation, an error response is returned with a status code of 400 (bad request). The response includes a message indicating that validation failed and the specific validation errors returned by the serializer.

 # Read (GET)
class NoteListView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Help function to get user object
    def get_object(self, note_id, user_id):
       try:
          return Note.objects.get(id=note_id, user=user_id)
       except Note.DoesNotExist:
          return None
       
       # Get by id
    def get(self, request, note_id, *args, **kwargs):
       note_instance = self.get_object(note_id, request.user.id)
       
       if not note_instance:
          return Response({'message': "object with note id does not exist"})
       serializer = NoteSerializer(note_instance)
       return Response (serializer.data)
          

class NoteDetailView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderNotesByLatestView(generics.ListAPIView):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

class FilterUnfinishedNotesView(generics.ListAPIView):
    queryset = Note.objects.filter(finished=False)
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

class FilterOverdueNotesView(generics.ListAPIView):
    queryset = Note.objects.filter(due_date__lt=timezone.now(), finished=False)
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

class FilterDoneNotesView(generics.ListAPIView):
    queryset = Note.objects.filter(finished=True)
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

 # Update (PUT)
class NoteUpdateView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

 # Delete (DELETE)
class NoteDeleteView(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

# Sorting all the notes list by due-date, priority, and created-time
class SortNotesByDueDateView(generics.ListAPIView):
    queryset = Note.objects.all().order_by('due_date')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['due_date']

class SortNotesByPriorityView(generics.ListAPIView):
    queryset = Note.objects.all().order_by('-priority')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['priority']

class SortNotesByCreatedTimeView(generics.ListAPIView):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']

def exportNotes_to_pdf(request):
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachement; filename="notes.pdf"'

   # Create a pdf document
   p = canvas.Canvas(response, pagesize=letter)
   notes = Note.objects.all()
   for note in notes:
      p.drawString(100, 700, note.title)
      p.drawString(100, 680, note.content)
      p.showPage()

   p.save()
   return response

def exportNotes_to_csv(request):
   response = HttpResponse(content_type='text/csv')
   response['Content-Disposition'] = 'attachement; filename="notes.csv"'

   writer = csv.writer(response)
   writer.writerow(['Title', 'Content'])
   notes = Note.objects.all()
   for note in notes:
      writer.writerow([note.title, note.content])

      return response
   
# Creating email function
def send_notesList_email(request):
   subject = 'Your Notes List'
   message = 'Here is your list of notes:'
   from_email = 'patience@gmail.com'
   recipient_list = ['recipient-email@gmail.com']
   attachment = ['notes.pdf', 'notes.csv'] # You can attach pdf or csv files if you've generated them
   # Using attachment parameter

   send_mail(subject, message, from_email, recipient_list, attachment)

class SwaggerView(APIView):
    @swagger_auto_schema(
        operation_summary="Summary of the operation",
        operation_description="Detailed description of the operation."
    )
    def get(self, request):
        """
        This docstring provides an overview of what the API does.
        ---
        parameters:
            - name: parameter_name
              in: query
              type: integer
              description: Description of the parameter
        """
        # Your view logic here
        return Response(request)