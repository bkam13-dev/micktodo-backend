from rest_framework import serializers
from tasks.models import Task

# serializer des tâches
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'slug', 'completed', 'created_at']
        read_only_fields = ['id', 'user', 'slug', 'created_at']
        
