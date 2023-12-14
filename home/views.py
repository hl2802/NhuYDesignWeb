from django.shortcuts import render
from django.http import HttpResponse
from .models import postImg 
from blog.models import postForm as bl
from portfolio.models import postForm as sp
from contact.models import contactForm 
from contact.forms import contact_Form 
from .models import subForm
# Create your views here.
def index(request):
    form = contact_Form()
    avt=postImg.objects.all()
    pF = bl.objects.all()
    pFF = sp.objects.all()
    return render(request,'home/index.html',{'avt':avt,'pF':pF,'pFF':pFF,'form':form})


def single_blog(request, id):
    pD = bl.objects.get(id=id)
    return render(request, 'home/index.html', {'pD': pD})
# @receiver(post_save, sender=postForm)

def single_blog(request, id):
    pDD = sp.objects.get(id=id)
    return render(request, 'home/index.html', {'pDD': pDD})
def getContact(request):
    if request.method == "POST":
        form = contact_Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/index.html')
        else:
            context = {'form': form}
            return render(request, 'contact/index.html', context)
    else:
        return HttpResponse("Error, not a POST request")
    
def saveContact(request):
    if request.method == "POST":
        form = contact_Form(request.POST)
        if form.is_valid():
            saveForm=subForm( email=form.cleaned_data['email'])
            saveContact.save()
           
            return render(request, 'home/index.html')
        else:
            context = {'form': form}
            return render(request, 'contact/index.html', context)
    else:
        return HttpResponse("Error, not a POST request")
