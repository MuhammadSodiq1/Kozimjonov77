# Generated by Django 4.1.3 on 2022-12-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
