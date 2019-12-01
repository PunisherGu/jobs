from django.db import models


class RequiredDegree(models.Model):
    id = models.IntegerField(primary_key=True)
    degree = models.CharField(
        max_length = 30,
        db_column = 'escolaridade',
        verbose_name = 'escolaridade',
    )

    class Meta:
        db_table = 'grau_minimo'
        verbose_name = 'grau mínimo exigido'

    def __str__(self):
        return self.degree


class SalaryRange(models.Model):
    id = models.IntegerField(primary_key=True)
    value1 = models.DecimalField(
        db_column='valor_base',
        max_digits=6,
        decimal_places=2,
        verbose_name='valor base da faixa',
    )
    value2 = models.DecimalField(
        db_column='valor_teto',
        max_digits=10,
        decimal_places=2,
        verbose_name='valor teto da faixa',
    )

    class Meta:
        db_table = 'faixa_salarial'
        verbose_name = 'Salario'

    def __str__(self):
        return f'{self.value1} até {self.value2}'


class CandidatesJobsApply(models.Model):
    candidate = models.ForeignKey(
        'users.Candidate',
        models.PROTECT,
        verbose_name='candidato',
        db_column='candidate_id',
    )
    job = models.ForeignKey(
        'Jobs',
        models.PROTECT,
        verbose_name='oportunidade',
        db_column='oportunidade_id'
    )
    salary_claim = models.DecimalField(
        db_column='pretensao_salarial',
        max_digits=10,
        decimal_places=2,
        verbose_name='pretensão salarial',
        blank=True,
        null=True
    )
    affinity = models.IntegerField(
        default=0,
        verbose_name='afinidade',
        db_column='afinidade x vaga'
    )

    class Meta:
        db_table = 'candidato_vaga'
        verbose_name = 'candidatos x vaga'


class Jobs(models.Model):
    job_name = models.CharField(
        max_length=150,
        db_column='nome_vaga',
        verbose_name='nome da vaga',
    )
    salary = models.ForeignKey(
        SalaryRange,
        models.PROTECT,
        verbose_name='Faixa salarial',
    )
    requirements = models.TextField(
        db_column='requisitos',
        verbose_name='requisitos',
    )
    required_degree = models.ForeignKey(
        RequiredDegree,
        models.PROTECT,
        verbose_name='Grau exigido',
    )
    candidates = models.ManyToManyField(
        'users.Candidate',
        blank=True,
        through=CandidatesJobsApply,
    )

    class Meta:
        db_table = 'vagas'
        verbose_name = 'vagas'

    def __str__(self):
        return self.job_name
