from datetime import date
from django.core.validators import MinValueValidator, MaxLengthValidator, MinLengthValidator
from django.db import models
from base.validators import Validators


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identification_code = models.PositiveIntegerField(validators=[MinValueValidator(2500)])

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class BusinessUser(models.Model):
    business_user_name = models.CharField(max_length=100)
    registry_number = models.PositiveIntegerField(validators=[Validators.validate_correct_registry_number])

    def __str__(self):
        return self.business_user_name


class Company(models.Model):
    name = models.CharField(max_length=100,
                            validators=[MaxLengthValidator(100), MinLengthValidator(3)])
    registry_number = models.PositiveIntegerField(default=date.today(),
                                                  validators=[Validators.validate_correct_registry_number])
    establishment_date = models.DateField(validators=[Validators.validate_not_future_date])
    total_capital = models.PositiveIntegerField(validators=[MinValueValidator(2500)])
    business_owners = models.ManyToManyField(BusinessUser, through='Ownership')
    individual_owners = models.ManyToManyField(User, through='Ownership')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Ownership(models.Model):
    is_founder = models.BooleanField(default=True)
    is_business_user = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    capital_size = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    business_user = models.ForeignKey(BusinessUser, null=True, blank=True, on_delete=models.CASCADE,
                                      related_name='business_user')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.business_user is None:
            return str(f"{self.user} - {self.company}")
        else:
            return str(f"{self.business_user} - {self.company}")

    class Meta:
        unique_together = ["company", "user", "business_user"]
