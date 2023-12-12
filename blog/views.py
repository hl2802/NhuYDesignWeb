from django.shortcuts import render
from django.http import HttpResponse
from .models import postForm
# Create your views here.
def index(request):
    pF = postForm.objects.all()
    return render(request, 'blog/index.html', {'pF': pF})
def single_blog(request, id):
    pD = postForm.objects.get(id=id)
    return render(request, 'blog/single_blog.html', {'pD': pD})