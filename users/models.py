from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from opportunities.models import RequiredDegree

class CustomUser(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)


class Candidate(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True
    )
    experiences = models.TextField(
        db_column = 'experiencias de trabalho',
        verbose_name = 'experiencias',
        null=True,
        blank=True
    )
    degree = models.ForeignKey(
        RequiredDegree,
        models.PROTECT,
        verbose_name='grau de formação',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'candidato'
        verbose_name = 'candidato'
        verbose_name_plural = 'candidatos'

    def __str__(self):
        return self.user.username


class Employer(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

    class Meta:
        db_table = 'empregador'
        verbose_name = 'empregador'
        verbose_name_plural = 'empregadores'

    def __str__(self):
        return self.user.username
