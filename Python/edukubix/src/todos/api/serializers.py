from rest_framework import serializers
from ..models import *
from users.api.serializers import UserSerializer

from django.contrib.auth import get_user_model
User=get_user_model()


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user=UserSerializer(read_only=True)
    todo = serializers.CharField(max_length=500)
    done = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Todo
    
    def create(self, validated_data):
        user = self.context['request'].user
        print(user)
        return Todo.objects.create(user=user,**validated_data)
    
    def update(self, instance, validated_data):
        instance.todo = validated_data.get('todo', instance.todo)
        instance.done = validated_data.get('done', instance.done)
        instance.save()
        return instance

