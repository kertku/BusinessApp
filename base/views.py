from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from base.forms import CompanyForm, UserForm, OwnershipForm
from base.models import Company, Ownership


def home(request):
    new_entries = Company.objects.all()[:10]
    new_updates = Company.objects.order_by("-updated")[:10]
    context = {"new_entries": new_entries, "new_updates": new_updates}
    return render(request, "base/home.html", context)


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


def search(request):
    search_result_company = None
    search_result_owner = None
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    r = request.GET.get('r') if request.GET.get('q') is not None else ''

    if r == "company":
        print("ell")
        search_result_company = Company.objects.filter(Q(name__icontains=q) | Q(registry_number__icontains=q))
        print(search_result_company)
    if r is "owner":
        search_result_owner = Company.objects.filter(Q(name__icontains=q) | Q(registry_number__icontains=q))

    context = {"search_result_company": search_result_company, "search_result_owner": search_result_owner, "q": q}
    return render(request, "base/search.html", context)
