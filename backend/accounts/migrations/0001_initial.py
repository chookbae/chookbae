# Generated by Django 3.2.12 on 2022-11-04 13:10

import accounts.models
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nickname', models.CharField(blank=True, max_length=11)),
                ('profile_image', imagekit.models.fields.ProcessedImageField(blank=True, default='user/default.png', null=True, upload_to=accounts.models.profile_image_path)),
                ('email', models.EmailField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
                ('points', models.IntegerField(default=0)),
                ('value', models.IntegerField(default=0)),
                ('login_count', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
