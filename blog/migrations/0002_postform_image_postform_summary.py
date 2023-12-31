# Generated by Django 5.0 on 2023-12-11 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postform',
            name='image',
            field=models.ImageField(blank=True, default='no-image.png', null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postform',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
