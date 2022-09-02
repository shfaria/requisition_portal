# Generated by Django 4.1 on 2022-08-25 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0018_remove_requisition_send_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition',
            name='send_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_be_sent_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='submitted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_be_sent_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
