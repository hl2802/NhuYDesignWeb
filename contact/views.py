from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import contact_Form
from .models import contactForm
from django.views import View
# Create your views here.
def index(request):
    form = contact_Form()
    context = {'form': form}
    return render(request, 'contact/index.html', context)

def getContact(request):
    if request.method == "POST":
        form = contact_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")  # Use reverse URL for cleaner code
        else:
            context = {'form': form}
            return render(request, 'contact/index.html', context)
    else:
        return HttpResponse("Error, not a POST request")
    
def saveContact(request):
    if request.method == "POST":
        form = contact_Form(request.POST)
        if form.is_valid():
            saveForm=contactForm(name=form.cleaned_data['name'], email=form.cleaned_data['email'], body=form.cleaned_data['body'])
            saveContact.save()
           
            return HttpResponse("success")  # Use reverse URL for cleaner code
        else:
            context = {'form': form}
            return render(request, 'contact/index.html', context)
    else:
        return HttpResponse("Error, not a POST request")
