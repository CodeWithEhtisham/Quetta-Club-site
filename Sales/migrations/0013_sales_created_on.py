# Generated by Django 4.0.3 on 2022-09-29 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0012_alter_sales_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
