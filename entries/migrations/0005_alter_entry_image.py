# Generated by Django 5.2.1 on 2025-05-27 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_alter_entry_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(default='defaults/entry.jpg', upload_to='media/entries/'),
        ),
    ]
