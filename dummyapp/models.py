from django.db import models

# Create your models here.

class Userdetails(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    contact_no = models.IntegerField()
    description = models.CharField(max_length=255)
