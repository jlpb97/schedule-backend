# Generated by Django 2.2.10 on 2020-03-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200330_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='full_name',
            field=models.CharField(default='', max_length=101),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professional',
            name='full_name',
            field=models.CharField(default='', max_length=101),
            preserve_default=False,
        ),
    ]
