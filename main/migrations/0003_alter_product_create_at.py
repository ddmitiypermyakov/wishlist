# Generated by Django 3.2.7 on 2021-09-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_at',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
    ]
