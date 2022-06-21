from django.shortcuts import render, redirect
from base.forms import CompanyForm, UserForm, OwnershipForm
from base.models import Company, Ownership


def business(request):
    businesses = Company.objects.all()
    context = {"businesses": businesses}
    return render(request, "base/businesses.html", context)


def company(request, pk):
    company_form = CompanyForm()
    company_object = Company.objects.get(pk=pk)
    business_owners = company_object.business_owners.all()
    individual_owners = company_object.individual_owners.all()
    context = {"company": company_object, "business_owners": business_owners, "individual_owners": individual_owners}
    return render(request, "base/company.html", context)


def company_form(request):
    company_form = CompanyForm()

    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        if company_form.is_valid():
            new_company = company_form.save()
            return redirect("company", pk=new_company.id)
    context = {"company_form": company_form, }
    return render(request, "base/company_form.html", context)
