from django.forms import ModelForm
from base.models import Company, User, Ownership, BusinessUser
from django import forms


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ("name", "registry_number", "establishment_date", "total_capital")
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "registry_number": forms.NumberInput(attrs={'class': 'form-control'}),
            "establishment_date": forms.DateInput(attrs={'class': 'form-control'}),
            "total_capital": forms.NumberInput(attrs={'class': 'form-control'})
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "identification_code")
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "identification_code": forms.NumberInput(attrs={'class': 'form-control'}),
        }


class OwnershipForm(ModelForm):
    class Meta:
        model = Ownership
        fields = ('capital_size',)
        widgets = {
            "capital_size": forms.NumberInput(attrs={'class': 'form-control'}),
        }


class BusinessUserForm(ModelForm):
    class Meta:
        model = BusinessUser
        fields = ('business_user_name', 'registry_number')
        widgets = {
            "business_user_name": forms.TextInput(attrs={'class': 'form-control'}),
            "registry_number": forms.NumberInput(attrs={'class': 'form-control'})
        }
