# Generated by Django 2.2.10 on 2020-03-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200315_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='document',
            field=models.CharField(help_text="e.g.: The person's ID number", max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='document',
            field=models.CharField(help_text="e.g.: The person's ID number", max_length=50, unique=True),
        ),
    ]