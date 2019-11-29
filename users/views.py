from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login
from django.shortcuts import redirect

from jobs.forms import CandidateSignUpForm, EmployerSignUpForm
from .models import CustomUser


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


class CandidateSignUpView(CreateView):
    model = CustomUser
    form_class = CandidateSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'candidato'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # return redirect('students:quiz_list')


class EmployerSignUpView(CreateView):
    model = CustomUser
    form_class = EmployerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'recrutador'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # return redirect('students:quiz_list')
