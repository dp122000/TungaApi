# Serializers allow you to convert complex data types (like Django models) into native Python data types (like dictionaries) that can be easily rendered into JSON.

# notes/serializers.py

from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        #fields = ["id", "title", "story", "created_at"]

