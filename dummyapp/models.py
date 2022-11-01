from django.db import models
# from django.core.validators import RegexValidator
# Create your models here.

class Userdetails(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    description = models.CharField(max_length=255)
