from tutorial.quickstart.models import ExampleModel
from rest_framework import serializers


class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ['flag']
