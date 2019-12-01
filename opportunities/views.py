from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.contrib import messages
import json

from .models import Jobs, CandidatesJobsApply
from .forms import OpportunitiesNewForm
from django.shortcuts import redirect

class OpportunitiesView(CreateView):
    model = Jobs
    form_class = OpportunitiesNewForm
    template_name = 'opportunities_new.html'

    def form_valid(self, form):
        if form.is_valid():
            opportunite = form.save(commit=False)
            opportunite.save()
            return redirect('/jobs/')
        else:
         form = PostForm()


def opportunities_list(request):
    opportunities = Jobs.objects.all()
    for opportunite in opportunities:
        opportunite.applications = opportunite.candidates.count()
    return render(request, 'opportunities_list.html', {'opportunities': opportunities})

def opportunity_detail(request, pk):
    opportunity = get_object_or_404(Jobs, pk=pk)
    return render(request, 'opportunity_detail.html', {'opportunity': opportunity})

def opportunity_edit(request, pk):
     opportunity = get_object_or_404(Jobs, pk=pk)
     if request.method == "POST":
         form = OpportunitiesNewForm(request.POST, instance=opportunity)
         if form.is_valid():
             opportunity = form.save(commit=False)
             opportunity.save()
             return redirect('opportunity_detail', pk=opportunity.pk)
     form = OpportunitiesNewForm(instance=opportunity)
     return render(request, 'opportunities_new.html', {'form': form})

def candidates_list(request, pk):
    candidatures = CandidatesJobsApply.objects.filter(job=pk).all()
    return render(request, 'candidates_list.html', {'candidatures': candidatures})

def opportunity_delete(request, pk):
    opportunity = get_object_or_404(Jobs, pk=pk)
    is_exist = CandidatesJobsApply.objects.filter(job=opportunity.id).exists()
    if is_exist:
        messages.info(request, 'Já existem candidaturas para esse vaga, não foi posisivel deletar.')
        return render(request, 'opportunities_list.html')
    opportunity.delete()
    return render(request, 'opportunities_list.html')
