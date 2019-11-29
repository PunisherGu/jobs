from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import User

from users.models import CustomUser, Candidate, Employer

class CandidateSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "first_name", "last_name" ,"password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_candidate = True
        user.username = user.email
        user.save()
        student = Candidate.objects.create(user=user)
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
