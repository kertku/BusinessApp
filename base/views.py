from django.http import Http404
from django.shortcuts import render, redirect
from base.forms import CompanyForm, UserForm, OwnershipForm
from base.models import Company, Ownership


def business(request):
    businesses = Company.objects.all()
    context = {"businesses": businesses}
    return render(request, "base/businesses.html", context)


def company(request, pk):
    company_form = CompanyForm()
    try:
        company_object = Company.objects.get(pk=pk)
        owning_details = Ownership.objects.filter(company__id=pk)
        context = {"company": company_object, "owning_details": owning_details}
    except Company.DoesNotExist:
        raise Http404
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


def user_partial(request):
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            return redirect("company", pk=new_user.id)
    context = {"user_form": user_form, }
    return render(request, "base/partial_views/_partial_user_form.html", context)
