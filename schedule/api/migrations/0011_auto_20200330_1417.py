# Generated by Django 2.2.10 on 2020-03-30 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200328_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Client'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='professional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Professional'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Service'),
        ),
    ]
