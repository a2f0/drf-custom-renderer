from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from django.conf.urls import include, url
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'example_model', views.ExampleModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
