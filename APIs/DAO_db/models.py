from django.db import models

# Tables User

class User_Rol(models.Model):
    rol = models.CharField(max_length=50)

class Country(models.Model):
    name = models.CharField(max_length=50)

class User(models.Model):
    fk_rol = models.ForeignKey(User_Rol, on_delete=models.CASCADE)
    fk_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cell_number = models.CharField(max_length=50)

# Models Product

class Kind_Product(models.Model):
    kind = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

class Resources(models.Model):
    url = models.URLField()
    description = models.CharField(max_length=500)

class License(models.Model):
    date_opening = models.DateField()
    date_closing = models.DateField()

class Technology(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

class Software_Product(models.Model):
    fk_kind_product = models.ForeignKey(Kind_Product, on_delete=models.CASCADE)
    fk_resources = models.ForeignKey(Resources, on_delete=models.CASCADE)
    fk_license = models.ForeignKey(License, on_delete=models.CASCADE)
    fk_technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    fk_developer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

# Tables Sale

class Store(models.Model):
    fk_product = models.ForeignKey(Software_Product, on_delete=models.CASCADE)
    repository_url = models.URLField()

class Stock(models.Model):
    fk_product = models.ForeignKey(Software_Product, on_delete=models.CASCADE)
    fk_developer = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

class Bank(models.Model):
    name = models.CharField(max_length=50)

class Sale(models.Model):
    fk_stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    fk_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    fk_bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    fk_client = models.ForeignKey(User, on_delete=models.CASCADE)

class History(models.Model):
    fk_date_record = models.DateField()
    fk_date_sale = models.DateField()
    fk_sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
