# Generated by Django 3.0 on 2022-04-01 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_site', '0020_auto_20220401_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribedUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
