# Generated by Django 2.0.8 on 2018-09-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuites', '0004_remove_tuite_liked_by'),
        ('users', '0005_user_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='liked_tuites',
            field=models.ManyToManyField(related_name='liked_by', to='tuites.Tuite'),
        ),
    ]
