# Generated by Django 3.2 on 2021-04-20 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20210420_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name='Цена'),
        ),
    ]
