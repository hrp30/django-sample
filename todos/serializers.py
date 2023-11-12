from rest_framework import serializers
from django.contrib.auth.models import User

from todos.models import Todo


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoListSerializer(serializers.ListSerializer):
    child = TodoSerializer()
