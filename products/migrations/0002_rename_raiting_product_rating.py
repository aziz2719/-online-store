# Generated by Django 3.2 on 2021-04-21 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='raiting',
            new_name='rating',
        ),
    ]
