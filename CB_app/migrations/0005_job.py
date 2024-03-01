# Generated by Django 5.0.2 on 2024-02-22 07:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CB_app', '0004_userprofile_job_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.TextField()),
                ('long_description', models.TextField(blank=True, null=True)),
                ('company_name', models.CharField(max_length=255)),
                ('company_address', models.CharField(blank=True, max_length=255, null=True)),
                ('company_zipcode', models.CharField(blank=True, max_length=255, null=True)),
                ('company_place', models.CharField(blank=True, max_length=255, null=True)),
                ('company_country', models.CharField(blank=True, max_length=255, null=True)),
                ('company_size', models.CharField(choices=[('size_1-9', '1-9'), ('size_10-49', '10-49'), ('size_50-99', '50-99'), ('size_100', '100+')], default='size_1-9', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('employed', 'Employed'), ('archived', 'Archived')], default='active', max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]