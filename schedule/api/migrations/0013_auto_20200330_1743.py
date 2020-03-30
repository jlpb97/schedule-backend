# Generated by Django 2.2.10 on 2020-03-30 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20200330_1510'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='client',
            index=models.Index(fields=['full_name'], name='api_client_full_na_5c0756_idx'),
        ),
        migrations.AddIndex(
            model_name='professional',
            index=models.Index(fields=['full_name'], name='api_profess_full_na_b44f30_idx'),
        ),
    ]
