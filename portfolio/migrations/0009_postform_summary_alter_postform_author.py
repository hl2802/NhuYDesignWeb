# Generated by Django 5.0 on 2023-12-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_postform_image'),
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
            field=models.CharField(max_length=50),
        ),
    ]