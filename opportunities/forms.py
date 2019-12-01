from django import forms

from .models import Jobs

class OpportunitiesNewForm(forms.ModelForm):

    class Meta:
        model = Jobs
        fields = [
            'job_name',
            'salary',
            'requirements',
            'required_degree'
        ]
