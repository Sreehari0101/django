# Generated by Django 4.2.4 on 2023-09-11 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='login',
            name='login_password',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Leave_apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.IntegerField()),
                ('reason', models.CharField(max_length=120)),
                ('leave_type', models.TextField(max_length=420)),
                ('on_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.leave_status')),
            ],
        ),
    ]