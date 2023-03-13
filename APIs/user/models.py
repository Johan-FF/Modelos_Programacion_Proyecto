from django.db import models

# Create your models here.
class User(models.Model):
    fk_rol = models.PositiveIntegerField()
    fk_country = models.PositiveIntegerField()
    fk_history = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cell_number = models.CharField(max_length=50)