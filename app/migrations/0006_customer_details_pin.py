# Generated by Django 3.2.5 on 2021-09-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_customer_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_details',
            name='pin',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
    ]
