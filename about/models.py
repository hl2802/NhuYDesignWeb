from django.db import models
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField

class postAbout(models.Model):

    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
class postTarget(models.Model):

    # Use FileField with FileExtensionValidator
    image = models.FileField(
        upload_to='media/',
        blank=True,
        null=True,
        default='no-image.png',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'])]
    )

