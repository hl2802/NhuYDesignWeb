# Generated by Django 5.0 on 2023-12-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='subForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='contactForm',
        ),
    ]
