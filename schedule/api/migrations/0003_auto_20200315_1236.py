# Generated by Django 2.2.10 on 2020-03-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200314_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='id_document',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='id_document',
        ),
        migrations.AddField(
            model_name='client',
            name='document',
            field=models.CharField(default='ff', help_text="e.g.: The person's ID number", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professional',
            name='document',
            field=models.CharField(default='ff', help_text="e.g.: The person's ID number", max_length=50),
            preserve_default=False,
        ),
    ]
