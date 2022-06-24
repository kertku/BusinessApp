from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from django.db import models


class Validation:
    registry_validation_message = "Registry number must contain seven digits!"
    registration_date_validation_message = "Registration date can not be future date!"


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identification_code = models.PositiveIntegerField(validators=[MinValueValidator(2500)])

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class BusinessUser(models.Model, Validation):
    business_user_name = models.CharField(max_length=100)
    registry_number = models.PositiveIntegerField(
        validators=[MinValueValidator(1000000, message=Validation.registry_validation_message),
                    MaxValueValidator(9999999, message=Validation.registry_validation_message)])

    def __str__(self):
        return self.business_user_name


class Company(models.Model, Validation):
    name = models.CharField(max_length=100,
                            validators=[MaxLengthValidator(100), MinLengthValidator(3)])
    registry_number = models.PositiveIntegerField(
        validators=[MinValueValidator(1000000, message=Validation.registry_validation_message),
                    MaxValueValidator(
                        9999999, message=Validation.registry_validation_message)])
    establishment_date = models.DateField(
        validators=[MaxValueValidator(date.today(), message=Validation.registration_date_validation_message)])
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
    is_business_user = models.BooleanField()
    is_founder = models.BooleanField()
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
