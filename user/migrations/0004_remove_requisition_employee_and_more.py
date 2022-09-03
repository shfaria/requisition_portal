# Generated by Django 4.1 on 2022-08-20 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_requisition_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisition',
            name='employee',
        ),
        migrations.AddField(
            model_name='requisition',
            name='from_employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topic_content_type', to='user.newuser'),
        ),
        migrations.AddField(
            model_name='requisition',
            name='to_employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topic_content_type2', to='user.newuser'),
        ),
    ]