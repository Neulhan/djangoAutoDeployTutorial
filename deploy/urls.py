from django.urls import path
from deploy import views

urlpatterns = [
    path("", views.default)
]