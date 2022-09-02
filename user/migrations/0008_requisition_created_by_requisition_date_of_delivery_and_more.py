# Generated by Django 4.1 on 2022-08-24 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_requisition_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition',
            name='created_by',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='requisition',
            name='date_of_delivery',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
