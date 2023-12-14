from django.shortcuts import render
from django.http import HttpResponse
from home.models import postImg 
# Create your views here.
def index(request):
    avt=postImg.objects.all()
    return render(request, 'about/index.html', {'avt':avt})