# Generated by Django 4.2.5 on 2023-10-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineNotes', '0003_auto_20231010_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='reminder_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
