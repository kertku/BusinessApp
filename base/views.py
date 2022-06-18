from django.shortcuts import render

from base.models import Company


def business(request):
    businesses = Company.objects.all()
    context = {"businesses": businesses}
    return render(request, "base/businesses.html", context)


def company(request, pk):
    company_object = Company.objects.get(pk=pk)
    context = {"company": company_object}
    return render(request, "base/company.html", context)
