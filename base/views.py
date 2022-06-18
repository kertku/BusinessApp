from django.shortcuts import render

from base.models import Company


def business(request):
    businesses = Company.objects.all()
    context = {"businesses": businesses}
    return render(request, "base/businesses.html", context)
