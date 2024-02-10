# myapp/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactFormSubmission

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactFormSubmission.objects.create(name=name, email=email, subject=subject, message=message)
        return HttpResponse("Your message has been sent. Thank you!")
    return render(request, 'index.html')
