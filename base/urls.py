from django.urls import path

from base import views

urlpatterns = [
    path('', views.business, name="businesses"),
    path("company/create/", views.company_form, name="company_form"),
    path("company/<str:pk>/", views.company, name="company")

]
