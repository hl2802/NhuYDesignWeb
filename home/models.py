from django.db import models
from django.core.validators import FileExtensionValidator
class postImg(models.Model):
    # Use FileField with FileExtensionValidator
    image = models.FileField(
        upload_to='media/',
        blank=True,
        null=True,
        default='no-image.png',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'])]
    )
class subForm(models.Model):
    email= models.EmailField()
    def __str__(self) :
        return self.email
