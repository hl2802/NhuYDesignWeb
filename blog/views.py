from django.dispatch import receiver
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import postForm
from .models import commentForm
from .form import comment_Form
from django.db.models.signals import post_save
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    pF = postForm.objects.all()
    return render(request, 'blog/index.html', {'pF': pF})
def single_blog(request, id):
    pD = postForm.objects.get(id=id)
    return render(request, 'blog/single_blog.html', {'pD': pD})
def list(request):
    pF = postForm.objects.all()
    paginator = Paginator(pF, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/index.html', {'posts': posts})
def submit_comment(request):
    if request.method == "POST":
        form = comment_Form(request.POST)
        if form.is_valid():
            # Assuming you have 'post_id' as a field in the comment form to identify the related post
            post_id = form.cleaned_data['post_id']
            post = get_object_or_404(Post, pk=post_id)

            comment, created = Comment.objects.get_or_create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                body=form.cleaned_data['body'],
                post=post,
            )

            post.comments_count = Comment.objects.filter(post=post).count()
            post.save()

            if created:
                return HttpResponse("success")
            else:
                return HttpResponse("Comment already exists")
        else:
            context = {'form': form}
            return render(request, 'blog/index.html', context)
    else:
        return HttpResponse("Error: This is not a POST request")
    
@receiver(post_save, sender=commentForm)
def update_post_comment_count(sender, instance, **kwargs):
    instance.post.comments_count += 1
    instance.post.save()