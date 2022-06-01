from attr import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

class userserializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=('username','email','password1','password2')