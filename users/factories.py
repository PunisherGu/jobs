import factory

from . import models
from opportunities import models as op_models

class UserEmployerFactory(factory.DjangoModelFactory):
    last_name = factory.Faker('name')
    username = factory.LazyAttribute(lambda o: o.email.split('@')[0])
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', '123456')
    is_active = True
    is_employer = True

    class Meta:
        model = models.CustomUser


class UserCandidateFactory(factory.DjangoModelFactory):
    last_name = factory.Faker('name')
    username = factory.LazyAttribute(lambda o: o.email.split('@')[0])
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', '123456')
    is_active = True
    is_candidate = True

    class Meta:
        model = models.CustomUser


class CandidateFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserCandidateFactory)
    experiences = factory.Faker('sentence')
    degree = factory.Iterator(op_models.RequiredDegree.objects.all())

    class Meta:
        model = models.Candidate


class EmployerFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserEmployerFactory)

    class Meta:
        model = models.Employer
