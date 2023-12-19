from django.shortcuts import render
from django.http import HttpResponse
from .models import postImg 
from services.models import postImg as imgCT
from blog.models import postForm as bl
from portfolio.models import postForm as sp
from contact.models import contactForm 
from contact.forms import contact_Form 
from about.models import postAbout
from .models import subForm
# Create your views here.
def index(request):
    pA=postAbout.objects.all()
    sF = subForm.objects.all()
    form = contact_Form()
    avt=postImg.objects.all()
    iC=imgCT.objects.all()
    pF = bl.objects.order_by('-created_at')[:4]
    pFF = sp.objects.order_by('-created_at')[:4]
    return render(request,'home/index.html',{'avt':avt,'pF':pF,'pFF':pFF,'form':form,'iC':iC,'sF':sF,'pA':pA})


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
