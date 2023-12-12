from django.shortcuts import render
from django.http import HttpResponse
from .models import postForm
# Create your views here.
def index(request):
    pF = postForm.objects.all()
    return render(request, 'portfolio/index.html', {'pF': pF})
def single_portfolio(request, id):
    pD = postForm.objects.get(id=id)
    return render(request, 'portfolio/single_portfolio.html', {'pD': pD})
