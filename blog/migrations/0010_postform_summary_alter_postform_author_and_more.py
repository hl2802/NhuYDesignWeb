# Generated by Django 5.0 on 2023-12-12 13:56

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_postform_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='postform',
            name='summary',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='postform',
            name='author',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='postform',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='postform',
            name='image',
            field=models.FileField(blank=True, default='no-image.png', null=True, upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'])]),
        ),
    ]