from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import ExampleModelSerializer

from .models import ExampleModel
class ExampleModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleModelSerializer

    def get_queryset(self):
        print("renderer classes: " + str(self.renderer_classes))
        print("default renderer classes: " + str(settings.REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES']))
        return self.queryset

    def create(self, request, *args, **kwargs):
        print("renderer classes: " + str(self.renderer_classes))
        print("default renderer classes: " + str(settings.REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES']))
        return super().create(request)


        