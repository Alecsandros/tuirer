# Generated by Django 2.1 on 2018-09-09 22:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180909_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='seguindo', to=settings.AUTH_USER_MODEL),
        ),
    ]
