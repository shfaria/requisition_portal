# Generated by Django 4.1 on 2022-08-25 13:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0019_requisition_send_to_alter_requisition_submitted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisition',
            name='send_to',
        ),
        migrations.AddField(
            model_name='requisition',
            name='send_to',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]