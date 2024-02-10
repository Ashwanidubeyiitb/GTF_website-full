# urls.py in myapp

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Example index view
    path('submit/', views.submit_contact_form, name='submit_contact_form'),  # URL pattern for submitting contact form
]
