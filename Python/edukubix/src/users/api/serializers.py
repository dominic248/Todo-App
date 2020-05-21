from rest_framework import serializers
from django.contrib.auth import get_user_model
User=get_user_model()

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username=serializers.CharField(max_length=500)
    email=serializers.EmailField()
    class Meta:
        model = User

