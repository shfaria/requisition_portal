# Generated by Django 4.1 on 2022-08-25 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_requisition_date_of_delivery_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisition',
            old_name='employee',
            new_name='send_to',
        ),
    ]
