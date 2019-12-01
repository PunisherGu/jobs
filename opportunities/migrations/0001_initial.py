# Generated by Django 2.2.7 on 2019-12-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidatesJobsApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_claim', models.DecimalField(blank=True, db_column='pretensao_salarial', decimal_places=2, max_digits=10, null=True, verbose_name='pretensão salarial')),
                ('affinity', models.IntegerField(db_column='afinidade x vaga', default=0, verbose_name='afinidade')),
            ],
            options={
                'verbose_name': 'candidatos x vaga',
                'db_table': 'candidato_vaga',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(db_column='nome_vaga', max_length=150, verbose_name='nome da vaga')),
                ('requirements', models.TextField(db_column='requisitos', verbose_name='requisitos')),
            ],
            options={
                'verbose_name': 'vagas',
                'db_table': 'vagas',
            },
        ),
        migrations.CreateModel(
            name='RequiredDegree',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('degree', models.CharField(db_column='escolaridade', max_length=30, verbose_name='escolaridade')),
            ],
            options={
                'verbose_name': 'grau mínimo exigido',
                'db_table': 'grau_minimo',
            },
        ),
        migrations.CreateModel(
            name='SalaryRange',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('value1', models.DecimalField(db_column='valor_base', decimal_places=2, max_digits=6, verbose_name='valor base da faixa')),
                ('value2', models.DecimalField(db_column='valor_teto', decimal_places=2, max_digits=10, verbose_name='valor teto da faixa')),
            ],
            options={
                'verbose_name': 'faixa salarial',
                'db_table': 'faixa_salarial',
            },
        ),
    ]
