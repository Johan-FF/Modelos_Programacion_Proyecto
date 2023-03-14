from django.db import models

class Kind_Product(models.Model):
    kind = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

class Resources(models.Model):
    name = models.CharField(max_length=50)
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
    name = models.CharField(max_length=50)