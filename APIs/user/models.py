from django.db import models

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

class User_Rol(models.Model):
    rol = models.CharField(max_length=50)

class Country(models.Model):
    name = models.CharField(max_length=50)

class History(models.Model):
    fk_date_record = models.DateField()
    fk_date_sale = models.DateField()
    fk_client = models.PositiveIntegerField()
    fk_developer = models.PositiveIntegerField()
    fk_sale = models.PositiveIntegerField()
    fk_bank = models.PositiveIntegerField()
    fk_history = models.PositiveIntegerField()