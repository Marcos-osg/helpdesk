# Generated by Django 3.2 on 2021-09-21 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210919_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='cidade',
            new_name='estado',
        ),
    ]
