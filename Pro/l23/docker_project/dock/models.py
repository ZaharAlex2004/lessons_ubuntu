from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
