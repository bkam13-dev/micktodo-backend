from rest_framework import serializers
from tasks.models import Task
from django.utils.text import slugify

# serializer des tâches
class TaskSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'slug', 'completed', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
        

    def update(self, instance, validated_data):
        # Si le titre est modifié, on regénère le slug
        if 'title' in validated_data:
            new_title = validated_data['title']
            
            # Générer un slug à partir du nouveau titre
            new_slug = slugify(new_title)
            validated_data['slug'] = new_slug

        # Appeler la méthode update du parent pour sauvegarder les changements
        return super().update(instance, validated_data)