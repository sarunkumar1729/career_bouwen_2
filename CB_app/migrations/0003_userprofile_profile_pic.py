# Generated by Django 5.0.2 on 2024-02-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_app', '0002_userprofile_company_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics/'),
        ),
    ]
