# Generated by Django 3.2.5 on 2021-07-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_books_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='img',
            field=models.ImageField(default=True, upload_to='books/images'),
        ),
    ]