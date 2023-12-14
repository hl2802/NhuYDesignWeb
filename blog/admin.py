from django.contrib import admin
from.models import postForm
from .models import commentForm
admin.site.register(commentForm)
admin.site.register(postForm)
