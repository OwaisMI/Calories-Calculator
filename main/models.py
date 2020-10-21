from django.db import models

# Create your models here.

class CalorieCal(models.Model):
    Age=models.IntegerField()
    Weight=models.IntegerField()
    Height=models.IntegerField()
    Activity=models.IntegerField()
