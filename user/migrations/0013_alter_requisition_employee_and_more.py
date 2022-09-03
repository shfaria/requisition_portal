# Generated by Django 4.1 on 2022-08-24 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_rename_created_by_requisition_submitted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='employee',
            field=models.ManyToManyField(to='user.newuser'),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='submitted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_be_sent_by', to='user.newuser'),
        ),
    ]