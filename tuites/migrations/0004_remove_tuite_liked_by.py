# Generated by Django 2.0.8 on 2018-09-08 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tuites', '0003_tuite_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tuite',
            name='liked_by',
        ),
    ]
