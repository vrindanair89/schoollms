from django.db import models

# Create your models here.

class Demo(models.Model):
    first_name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    contact=models.IntegerField()

