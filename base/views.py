from django.db.models import Q
from django.forms import modelformset_factory
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from base.forms import CreateCompany, OwnershipForm, BusinessOwnershipForm
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
    OwnershipFormset = modelformset_factory(Ownership, form=OwnershipForm, extra=1)
    BusinessOwnershipFormset = modelformset_factory(Ownership, form=BusinessOwnershipForm, extra=1)
    create_company_form = CreateCompany(request.POST or None)
    new_company = create_company_form.save(False)
    queryset = Ownership.objects.filter(company=new_company)
    formset = OwnershipFormset(request.POST or None, queryset=queryset)
    business_formset = (BusinessOwnershipFormset(request.POST or None, queryset=queryset))
    if create_company_form.is_valid():
        new_company = create_company_form.save()
        ownerships = formset.save(commit=False)
        business_ownerships = business_formset.save(commit=False)
        for ownership in ownerships:
            ownership.is_business_user = False
            ownership.company = new_company
            ownership.is_founder = True
            ownership.save()
        for business_ownership in business_ownerships:
            business_ownership.is_business_user = True
            business_ownership.company = new_company
            business_ownership.is_founder = True
            business_ownership.save()
        return redirect("company", pk=new_company.id)
    context = {"create_company_form": create_company_form, 'formset': formset, "business_formset": business_formset}
    return render(request, "base/company_form.html", context)


def search(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    search_result = Company.objects.filter(
        Q(name__icontains=q) | Q(registry_number__icontains=q) | Q(individual_owners__first_name__icontains=q) | Q(
            individual_owners__identification_code__icontains=q)).distinct()
    context = {"search_result": search_result, "q": q}
    return render(request, "base/search.html", context)
