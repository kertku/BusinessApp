from django.forms import ModelForm, formset_factory
from base.models import Company, User, Ownership, BusinessUser
from django import forms
from base.widget import DatePickerInput


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
        fields = ('capital_size', 'user',)
        widgets = {
            'user': forms.Select(attrs={'class': 'form-group row'}),
            "capital_size": forms.NumberInput(attrs={'class': 'form-group row'}),
        }


class BusinessUserForm(ModelForm):
    class Meta:
        model = BusinessUser
        fields = ('business_user_name', 'registry_number')
        widgets = {
            "business_user_name": forms.TextInput(attrs={'class': 'form-control'}),
            "registry_number": forms.NumberInput(attrs={'class': 'form-control'})
        }


class CreateCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("name", "registry_number", "establishment_date", "total_capital")
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "registry_number": forms.NumberInput(attrs={'class': 'form-control'}),
            "establishment_date": DatePickerInput(attrs={'class': 'form-control'}),
            "total_capital": forms.NumberInput(attrs={'class': 'form-control'})
        }
