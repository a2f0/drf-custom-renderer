from django.db import models
class ExampleModel(models.Model):
    flag =  models.BooleanField(default=False)

    class Meta:
        app_label  = 'quickstart'
