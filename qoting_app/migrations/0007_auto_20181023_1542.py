# Generated by Django 2.1.2 on 2018-10-23 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qoting_app', '0006_auto_20181023_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
