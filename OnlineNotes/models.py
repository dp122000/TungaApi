from django.db import models
from rest_framework import serializers
# Create your models 
from django.contrib.auth.models import User  # Using Django's built-in User model
#from OnlineNotes.models import Category

# This model represents a note with fields for the user it belongs to, title, content, creation date, due date, priority, status and update date.
class Category(models.Model):
    #id = models.AutoField(primary_key=True)  # Ensure the primary key is defined
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, max_length=1000)

    def __str__(self):
        return self.name

from OnlineNotes.models import Category

class Note(models.Model):
    title = models.CharField(max_length=255)
    story = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(default=True)
    finished = models.BooleanField(default=False)
    priority = models.CharField(max_length=20, default=True)
    status = models.CharField(max_length=20, default=True)
    reminder_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class NoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    created_at = serializers.DateField(read_only=True)