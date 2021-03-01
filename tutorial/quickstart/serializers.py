from django.contrib.auth.models import User, Group
from rest_framework import serializers


class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['flag']
