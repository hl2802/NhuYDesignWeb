# Generated by Django 5.0 on 2023-12-16 14:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posttarget',
            name='author',
        ),
        migrations.RemoveField(
            model_name='posttarget',
            name='body',
        ),
        migrations.RemoveField(
            model_name='posttarget',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='posttarget',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='posttarget',
            name='title',
        ),
        migrations.AlterField(
            model_name='postabout',
            name='body',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
