# Generated by Django 3.2.12 on 2022-10-27 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worldcup', '0004_alter_prediction_bet_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bet',
            old_name='loss',
            new_name='lose',
        ),
    ]
