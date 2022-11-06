# Generated by Django 4.1.2 on 2022-11-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webadmin', '0008_film_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='film',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]