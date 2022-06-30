from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from base.forms import CreateCompany, OwnershipForm
from base.models import Company, Ownership, User
from django.forms.formsets import BaseFormSet


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


class AddUserFormset(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return


def company_form(request, ):
    create_company_form = CreateCompany()
    create_ownership_form = OwnershipForm()
    if request.method == 'POST':
        company_form = CreateCompany(request.POST or None)
        create_ownership_form = OwnershipForm(request.POST or None)
        if company_form.is_valid():
            new_company = company_form.save()
            ownership = create_ownership_form.save(commit=False)
            ownership.is_business_user = False
            ownership.company = new_company
            ownership.is_founder = True
            ownership.save()
            return redirect("company", pk=new_company.id)
    context = {"create_company_form": create_company_form, "create_ownership_form": create_ownership_form, }
    return render(request, "base/company_form.html", context)


def search(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    search_result = Company.objects.filter(
        Q(name__icontains=q) | Q(registry_number__icontains=q) | Q(individual_owners__first_name__icontains=q) | Q(
            individual_owners__identification_code__icontains=q)).distinct()
    context = {"search_result": search_result, "q": q}
    return render(request, "base/search.html", context)
