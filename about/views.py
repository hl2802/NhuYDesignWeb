from django.shortcuts import render
from django.http import HttpResponse
from home.models import postImg 
from .models import postAbout
from .models import postTarget
# Create your views here.
def index(request):
    pA = postAbout.objects.all()
    pTG = postTarget.objects.all()
    avt=postImg.objects.all()
    return render(request, 'about/index.html', {'avt':avt,'pA':pA, 'pTG':pTG})