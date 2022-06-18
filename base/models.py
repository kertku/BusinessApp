from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100,
                            validators=[MaxLengthValidator(100), MinLengthValidator(3)])
    registry_number = models.PositiveIntegerField(validators=[MinValueValidator(1000000), MaxValueValidator(9999999)])
    establishment_date = models.DateField(validators=[MaxValueValidator(date.today())])
    total_capital = models.PositiveIntegerField(validators=[MinValueValidator(2500)])

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identification_code = models.PositiveIntegerField(validators=[MinValueValidator(2500)])

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class BusinessUser(models.Model):
    business_user_name = models.CharField(max_length=100)
    registry_number = models.PositiveIntegerField(validators=[MinValueValidator(1000000), MaxValueValidator(9999999)])

    def __str__(self):
        return self.business_user_name


class Owner(models.Model):
    is_founder = models.BooleanField()
    is_business_user = models.BooleanField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    business_user = models.ForeignKey(BusinessUser, null=True, blank=True, on_delete=models.CASCADE,
                                      related_name='business_user')

    def __str__(self):
        if self.is_business_user:
            return str(self.business_user)
        else:
            return str(self.user)


class Ownership(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    capital_size = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        unique_together = ["company", "owner"]
