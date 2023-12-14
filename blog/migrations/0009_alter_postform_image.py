# Generated by Django 5.0 on 2023-12-12 09:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_postform_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postform',
            name='image',
            field=models.FileField(blank=True, default='no-image.png', null=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'])]),
        ),
    ]
