# Generated by Django 3.0 on 2022-03-31 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_site', '0010_auto_20220331_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_cost',
            field=models.IntegerField(),
        ),
    ]
