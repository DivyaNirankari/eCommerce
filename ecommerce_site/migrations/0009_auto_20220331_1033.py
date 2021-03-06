# Generated by Django 3.0 on 2022-03-31 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_site', '0008_auto_20220330_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_cost',
        ),
        migrations.AddField(
            model_name='cart',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce_site.Cart'),
        ),
    ]
