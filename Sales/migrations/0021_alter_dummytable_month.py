# Generated by Django 4.0.3 on 2022-10-04 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0020_alter_dummytable_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummytable',
            name='month',
            field=models.DateField(),
        ),
    ]
