# Generated by Django 3.2.18 on 2023-03-19 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/user_avatar'),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
