# Generated by Django 3.2.5 on 2021-07-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='img',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]
