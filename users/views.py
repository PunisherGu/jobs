from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from decimal import Decimal

from jobs.forms import CandidateSignUpForm, EmployerSignUpForm, CandidatureForm
from .models import CustomUser, Candidate
from opportunities.models import CandidatesJobsApply, Jobs


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
        return redirect('/jobs/')


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
        return redirect('/jobs/')


def candidature_apply(request, pk):
     if request.method == 'POST':
         affinity = 0
         user = get_object_or_404(Candidate, pk=request.user.id)
         opportunity = get_object_or_404(Jobs, pk=pk)
         salary_claim = request.POST['salary_claim']
         salary_claim = Decimal(salary_claim)
         if user.degree.id >= opportunity.required_degree.id:
             affinity +=1
         if salary_claim > opportunity.salary.value1 and salary_claim < opportunity.salary.value2:
             affinity +=1
         response = CandidatesJobsApply.objects.create(
            candidate=user,
            job=opportunity,
            salary_claim=salary_claim,
            affinity=affinity
         )
         if response:
             return render(request, 'candidature_success.html')

     opportunity = get_object_or_404(Jobs, pk=pk)
     form = CandidatureForm(instance=opportunity)
     return render(request, 'candidature_apply.html', {'form': form, 'opportunity': opportunity})
