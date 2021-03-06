# Generated by Django 3.0 on 2022-03-30 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_site', '0007_cart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='addresss',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='zipcode',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('addresss', models.TextField(default='address', max_length=500)),
                ('city', models.TextField(default='city', max_length=20)),
                ('zipcode', models.IntegerField(default=0)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('delivered_by', models.DateTimeField()),
                ('order_status', models.CharField(choices=[('pending', 'pending'), ('delivered', 'delivered')], max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_site.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
