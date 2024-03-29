# Generated by Django 4.1.3 on 2022-12-28 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_comments_blogtitle_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comment',
            new_name='text',
        ),
        migrations.AddField(
            model_name='comments',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='fname',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='lname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
