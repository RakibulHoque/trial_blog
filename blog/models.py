from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    instit = models.TextField()
    img = models.ImageField(upload_to='uploaded_imgs')
    designation = models.BooleanField(default=False)
