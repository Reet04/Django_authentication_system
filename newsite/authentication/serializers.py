
from rest_framework import serializers

class self_serializer(serializers.Serializer):
    username=serializers.CharField(max_length=200)
    email=serializers.CharField(max_length=100)
    first_name=serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)
    email=serializers.CharField(max_length=100)
    last_login=serializers.CharField(max_length=100)
    is_staff=serializers.BooleanField()
