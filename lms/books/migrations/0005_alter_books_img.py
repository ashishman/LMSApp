# Generated by Django 3.2.5 on 2021-07-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_books_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='img',
            field=models.ImageField(upload_to='books/images'),
        ),
    ]
