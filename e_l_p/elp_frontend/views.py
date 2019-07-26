from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegistrationFormModed

class SignUp(generic.CreateView):
    form_class = RegistrationFormModed
    success_url = 'elp/login/'
    template_name = 'signup.html'
