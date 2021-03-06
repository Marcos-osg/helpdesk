# Generated by Django 3.2.7 on 2021-09-22 10:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
        ('accounts', '0001_initial'),
        ('tecnicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('descricao_servico', models.TextField(verbose_name='Descrição do Serviço')),
                ('tipo_servico', models.CharField(choices=[('Manutenção', 'Manutenção'), ('Troca', 'Troca'), ('Formatacao', 'Formatação'), ('Backup', 'Backup')], max_length=25, verbose_name='Tipo de Serviço')),
                ('data_servico', models.DateField(auto_now=True, verbose_name='Data de Inicio')),
                ('data_entrega', models.DateField(verbose_name='Data prevista')),
                ('status', models.CharField(choices=[('Nao finalizado', 'Não Finalizado'), ('Finalizado', 'Finalizado')], max_length=25)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cliente', to='accounts.cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='produto', to='produtos.produto')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tecnico', to='tecnicos.tecnico')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
    ]
