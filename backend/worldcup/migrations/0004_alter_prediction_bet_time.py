# Generated by Django 3.2.12 on 2022-10-27 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldcup', '0003_auto_20221027_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='bet_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
