# Generated by Django 4.0 on 2022-11-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0030_alter_bill_sale_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='bill_status',
            field=models.BooleanField(default=False),
        ),
    ]
