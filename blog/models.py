from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
# Create your models here.
class postForm(models.Model):
    title = models.CharField(max_length=50)

    # Use FileField with FileExtensionValidator
    image = models.FileField(
        upload_to='media/',
        blank=True,
        null=True,
        default='no-image.png',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'])]
    )
    summary = models.CharField(max_length=200,null=True)
    body = RichTextField()
    author = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class commentForm(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name
