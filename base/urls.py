from django.urls import path

from base import views

urlpatterns = [
    path('', views.home, name="home"),
    path("company/create/", views.company_form, name="company_form"),
    path("company/search/", views.search, name="search"),
    path("company/<str:pk>/", views.company, name="company"),


]
