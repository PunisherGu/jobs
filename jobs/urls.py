"""jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from opportunities import views as opportunitiesViews
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/candidate/', userViews.CandidateSignUpView.as_view(), name='candidate_signup'),
    path('accounts/signup/employer/', userViews.EmployerSignUpView.as_view(), name='employer_signup'),
    path('jobs/', opportunitiesViews.opportunities_list, name='opportunities_list'),
    path('jobs/new/', opportunitiesViews.OpportunitiesView.as_view(), name='opportunities_new'),
    path('jobs/<int:pk>/', opportunitiesViews.opportunity_detail, name='opportunity_detail'),
    path('jobs/<int:pk>/edit/', opportunitiesViews.opportunity_edit, name='opportunity_edit'),
    path('jobs/<int:pk>/delete/', opportunitiesViews.opportunity_delete, name='opportunity_delete'),
    path('candidature/<int:pk>/', userViews.candidature_apply, name='candidature_apply'),
    path('candidature_success',TemplateView.as_view(template_name='candidature_success.html'), name='candidature_success'),
    path('candidates_list/<int:pk>', opportunitiesViews.candidates_list, name='candidates_list'),
    path('opportunities/chart', opportunitiesViews.opportunities_by_month, name='opportunities_by_month'),
    path('candidates/chart', opportunitiesViews.candidates_by_month, name='candidates_by_month'),
]
