from django.db import models
from django.db import connections

class User(models.Model):
    username = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    emailid = models.CharField(max_length=255, primary_key=True) 
    password = models.CharField(max_length=255)
    class Meta:
        db_table="userdetail"