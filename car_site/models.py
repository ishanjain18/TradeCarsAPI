from django.db import models
from django.db.models.deletion import CASCADE

class Companies(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self) -> str:
        return self.name

class Cars(models.Model):
    name = models.CharField(max_length=250)
    company = models.ForeignKey(Companies, on_delete=CASCADE)
    def __str__(self) -> str:
        return self.name

class Sellers(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Listings(models.Model):

    make = models.ForeignKey(Companies, on_delete=CASCADE)
    model_name = models.ForeignKey(Cars, on_delete=CASCADE)
    seller = models.ForeignKey(Sellers, on_delete=CASCADE)
    # car_image todo
    purchase_year = models.PositiveSmallIntegerField()
    min_price = models.DecimalField(max_digits=5, decimal_places=2)
    max_price = models.DecimalField(max_digits=5, decimal_places=2)