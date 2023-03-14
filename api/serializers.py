from rest_framework import serializers
from .models import FeedbackUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackUser
        fields = [
            "name",
            "email",
            "phone",
            "message",
            "dateCreated",
            "get_absolute_url",
        ]