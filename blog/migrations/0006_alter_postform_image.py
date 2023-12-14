# Generated by Django 5.0 on 2023-12-12 08:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_postform_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postform',
            name='image',
            field=models.ImageField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp'])]),
        ),
    ]
