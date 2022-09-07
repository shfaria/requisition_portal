# Generated by Django 4.1 on 2022-09-06 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0031_remove_multinote_written_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='multinote',
            name='written',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='written', to='user.newuser'),
        ),
    ]