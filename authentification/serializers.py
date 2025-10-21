from rest_framework import serializers
from authentification.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'bio', 'profil_image']