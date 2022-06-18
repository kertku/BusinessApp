from django.shortcuts import render

from base.models import Business


def business(request):
    businesses = Business.objects.all()
    context = {"businesses": businesses}
    return render(request, "base/businesses.html", context)
