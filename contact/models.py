from django.db import models

# Create your models here.
class contactForm(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField()
    body= models.TextField()
    
    def __str__(self) :
        return self.name