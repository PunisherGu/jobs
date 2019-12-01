from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import User
from decimal import Decimal

from users.models import CustomUser, Candidate, Employer
from opportunities import models

class CandidateSignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Email'
    )
    degree = forms.ModelMultipleChoiceField(
        queryset= models.RequiredDegree.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Grau de formação'
    )
    expirence = forms.CharField(
        required=True,
        label='Experiência',
        widget=forms.Textarea,
    )


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            "email",
            "first_name",
            "last_name" ,
            "password1",
            "password2",
        ]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_candidate = True
        user.username = user.email
        user.save()
        candidate = Candidate.objects.create(user=user)
        degree=self.cleaned_data.get('degree')
        expirence=self.cleaned_data.get('expirence')
        candidate.experiences=expirence
        candidate.degree=degree[0]
        candidate.save()
        return user


class EmployerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "first_name", "last_name" ,"password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employer = True
        user.username = user.email
        user.save()
        student = Employer.objects.create(user=user)
        return user

class CandidatureForm(forms.ModelForm):
    class Meta:
        model = models.CandidatesJobsApply
        fields = ('salary_claim',)

    @transaction.atomic
    def save(self):
        import pdb; pdb.set_trace()
        # user = super().save(commit=False)
        # user.is_employer = True
        # user.username = user.email
        # user.save()
        # student = Employer.objects.create(user=user)
        return user
