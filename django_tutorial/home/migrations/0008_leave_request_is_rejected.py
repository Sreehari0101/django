# Generated by Django 4.2.4 on 2023-09-15 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_leave_request_delete_leave_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_request',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
    ]
