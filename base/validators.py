from django.core.exceptions import ValidationError
from django.utils.datetime_safe import date


class Validators:

    @staticmethod
    def validate_correct_registry_number(value):
        if 9999999 < value or value < 1000000:
            raise ValidationError("Registry number must contain seven digits!")
        else:
            return value

    @staticmethod
    def validate_not_future_date(value):
        if value > date.today():
            raise ValidationError("Date can´t be a future date!")
        else:
            return value
