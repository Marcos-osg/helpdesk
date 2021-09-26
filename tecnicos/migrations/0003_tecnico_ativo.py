# Generated by Django 3.2.7 on 2021-09-26 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnicos', '0002_alter_tecnico_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tecnico',
            name='ativo',
            field=models.CharField(choices=[('ATIVO', 'Ativo'), ('INATIVO', 'Inativo')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]