import factory

from users import factories
from . import models


class JobsFactory(factory.DjangoModelFactory):
    job_name = factory.Faker('job')
    salary = factory.Iterator(models.SalaryRange.objects.all())
    requirements = factory.Faker('sentence')
    required_degree = factory.Iterator(models.RequiredDegree.objects.all())

    class Meta:
        model = models.Jobs

class CandidatesJobsApplyFactory(factory.DjangoModelFactory):
    candidate = factory.SubFactory(factories.CandidateFactory)
    job = factory.SubFactory(JobsFactory)
    salary_claim = factory.Faker('random_int', min=1, max=50000)

    class Meta:
        model = models.CandidatesJobsApply
