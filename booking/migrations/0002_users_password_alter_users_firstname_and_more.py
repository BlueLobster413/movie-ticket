# Generated by Django 4.1.2 on 2022-11-01 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='firstname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastname',
            field=models.CharField(default='', max_length=20),
        ),
    ]