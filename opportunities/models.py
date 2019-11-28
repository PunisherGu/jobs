from django.db import models


class RequiredDegree(models.Model):
    id = models.IntegerField(primary_key=True)
    degree = models.CharField(
        max_length = 30,
        db_column = 'escolaridade',
        verbose_name = 'escolaridade',
    )


class SalaryRange(models.Model):
    id = models.IntegerField(primary_key=True)
    value1 = models.DecimalField(
        db_column='valor_base',
        max_digits=5,
        decimal_places=2,
        verbose_name='valor base da faixa',
    )
    value2 = models.DecimalField(
        db_column='valor_teto',
        max_digits=8,
        decimal_places=2,
        verbose_name='valor teto da faixa',
    )


class Jobs(models.Model):
    job_name = models.CharField(
        max_length=150,
        db_column='nome_vaga',
        verbose_name='nome da vaga',
    )
    salary = models.ForeignKey(
        SalaryRange,
        models.PROTECT,
    )
    requirements = models.TextField(
        db_column='requisitos',
        verbose_name='requisitos',
    )
    required_degree = models.ForeignKey(
        RequiredDegree,
        models.PROTECT,
    )
