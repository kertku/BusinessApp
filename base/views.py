from django.shortcuts import render, redirect
from base.forms import CompanyForm, UserForm, OwnerForm, OwnershipForm
from base.models import Company, Ownership, Owner


def business(request):
    businesses = Company.objects.all()
    context = {"businesses": businesses}
    return render(request, "base/businesses.html", context)


def company(request, pk):
    company_object = Company.objects.get(pk=pk)
    ownerships = Ownership.objects.filter(company_id=pk).all()
    context = {"company": company_object, "ownerships": ownerships}
    return render(request, "base/company.html", context)


def company_form(request):
    company_form = CompanyForm()
    user_form = UserForm()
    ownership_form = OwnershipForm()
    owner_form = OwnerForm()
    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        user_form = UserForm(request.POST)
        ownership_form = OwnershipForm(request.POST)
        if company_form.is_valid() and user_form.is_valid():
            new_company = company_form.save()
            new_user = user_form.save()
            owner_form.user = new_user
            new_owner = owner_form.save(False)
            new_owner.is_business_user = False
            new_owner.user = new_user
            new_owner.save()
            new_ownership = ownership_form.save(False)
            new_ownership.owner = new_owner
            new_ownership.company = new_company
            new_ownership.is_founder = True
            new_ownership.save()
            return redirect("company", pk=new_company.id)
    context = {"company_form": company_form, "user_form": user_form, "ownership_form": ownership_form,
               "owner_form": owner_form}
    return render(request, "base/company_form.html", context)
