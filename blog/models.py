from django.db import models

# Create your models here.
class postForm(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='no-image.png')
    body = models.TextField()
    author = models.TextField(blank=True)  # Nội dung tóm tắt
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

