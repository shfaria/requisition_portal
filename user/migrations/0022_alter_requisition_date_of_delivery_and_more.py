# Generated by Django 4.1 on 2022-08-27 04:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_alter_requisition_date_of_delivery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='date_of_delivery',
            field=models.DateField(blank=True, default=datetime.date(2022, 8, 27), null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='status',
            field=models.CharField(blank=True, choices=[('Processing', 'Processing'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
