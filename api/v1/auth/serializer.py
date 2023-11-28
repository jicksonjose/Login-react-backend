from rest_framework import serializers
from loginapp.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'name',
            'phone',
            'email',
            'password'
        )