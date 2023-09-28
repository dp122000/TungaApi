from django.db import models
from rest_framework import serializers
# Create your models 
from django.contrib.auth.models import User  # Using Django's built-in User model

# This model represents a note with fields for the user it belongs to, title, content, creation date, due date, priority, status and update date.

class Note(models.Model):
    title = models.CharField(max_length=200)
    story = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    due_date = models.DateField()
    priority = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    created_at = serializers.DateField(read_only=True)