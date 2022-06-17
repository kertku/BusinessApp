from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Business(models.Model):
    business_name = models.CharField(max_length=100, min_length=3,
                                     validators=[MinValueValidator(3), MaxValueValidator(100)])
    registry_number = models.PositiveIntegerField(validators=[MinValueValidator(1000000), MaxValueValidator(9999999)])
    establishment_date = models.DateField(validators=[MaxValueValidator(date.today())])
    total_capital = models.PositiveIntegerField(validators=[MinValueValidator(2500)])


class Owner(models.Model):
    is_founder = models.BooleanField()


class Ownership(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    capital_size = models.PositiveIntegerField(validators=[MinValueValidator(1)])
