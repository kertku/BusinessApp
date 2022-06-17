from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Business(models.Model):
    business_name = models.CharField(max_length=100,
                                     validators=[MinValueValidator(3), MaxValueValidator(100)])
    registry_number = models.PositiveIntegerField(validators=[MinValueValidator(1000000), MaxValueValidator(9999999)])
    establishment_date = models.DateField(validators=[MaxValueValidator(date.today())])
    total_capital = models.PositiveIntegerField(validators=[MinValueValidator(2500)])

    def __str__(self):
        return self.business_name


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identification_code = models.PositiveIntegerField(validators=[MinValueValidator(2500)])

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class BusinessUser(models.Model):
    business_user_name = models.CharField(max_length=100)
    registry_number = models.PositiveIntegerField(validators=[MinValueValidator(1000000), MaxValueValidator(9999999)])


class Owner(models.Model):
    is_founder = models.BooleanField()
    is_business_user = models.BooleanField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    business_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,
                                      related_name='business_user')


class Ownership(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    capital_size = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        unique_together = ["business", "owner"]
