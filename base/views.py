from django.db.models import Q
from django import forms
from django.http import Http404
from django.shortcuts import render, redirect
from base.forms import  CreateCompany
from base.models import Company, Ownership


def home(request):
    new_entries = Company.objects.all()[:10]
    new_updates = Company.objects.order_by("-updated")[:10]
    context = {"new_entries": new_entries, "new_updates": new_updates}
    return render(request, "base/home.html", context)


def company(request, pk):
    try:
        company_object = Company.objects.get(pk=pk)
        owning_details = Ownership.objects.filter(company__id=pk)
        context = {"company": company_object, "owning_details": owning_details}
    except Company.DoesNotExist:
        raise Http404
    return render(request, "base/company.html", context)


def company_form(request):
    company_form = CreateCompany()
    if request.method == 'POST':
        company_form = CreateCompany(request.POST)
        if company_form.is_valid():
            owners = company_form.cleaned_data.get('individual_owners')
            business_owners = company_form.cleaned_data.get('business_owners')
            new_company = company_form.save()
            for owner in owners:
                new_company.individual_owners.add(owner, through_defaults={"capital_size": 100, "is_founder": True,
                                                                           "is_business_user": False})
            for business_owner in business_owners:
                new_company.business_owners.add(business_owner, through_defaults={"capital_size": 100, "is_founder": True,
                                                                              "is_business_user": True})

            return redirect("company", pk=new_company.id)
    context = {"company_form": company_form, }
    return render(request, "base/company_form.html", context)


def search(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    search_result = Company.objects.filter(
        Q(name__icontains=q) | Q(registry_number__icontains=q) | Q(individual_owners__first_name__icontains=q) | Q(
            individual_owners__identification_code__icontains=q))
    context = {"search_result": search_result, "q": q}
    return render(request, "base/search.html", context)
