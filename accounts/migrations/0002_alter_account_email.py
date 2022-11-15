# Generated by Django 4.1.2 on 2022-11-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Email Address'),
        ),
    ]