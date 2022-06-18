from django.urls import path

from base import views

urlpatterns = [
    path('', views.business, name="businesses")
    #path("business/<str:pk>/", views.room, name="business"),
]
