from django.db import models

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

class User(models.Model):
    fk_rol = models.ForeignKey(User_Rol, on_delete=models.CASCADE)
    fk_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    fk_history = models.ForeignKey(History, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cell_number = models.CharField(max_length=50)