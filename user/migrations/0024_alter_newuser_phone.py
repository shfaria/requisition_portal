# Generated by Django 4.1 on 2022-09-02 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_alter_requisition_date_of_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
