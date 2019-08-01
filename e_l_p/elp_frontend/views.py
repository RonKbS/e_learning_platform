import os

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


from api.models.courses import Course
from .forms import (
    RegistrationFormModed,
    CurriculumPackageFormModed,
    CourseFormModed
)

base_url = os.getenv('BASE_URL', 'http://127.0.0.1:8000/')

def landing_page(request):
	return render(request, 'landing_page.html')


class SignUp(generic.CreateView):
    form_class = RegistrationFormModed
    success_url = reverse_lazy('index')
    template_name = 'signup.html'

    def form_valid(self, form):
        # by passing the checks coz of an error raise on line below:
        # "/Users/stephenbamwite/.local/share/virtualenvs/e_learning_platform-B-QMsOoK/lib/python3.7/site-packages/django/views/generic/edit.py", line 113
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(base_url + 'elp/login/')


class CurriculumView(LoginRequiredMixin, generic.edit.FormMixin):
    model = Course

    form_class = CurriculumPackageFormModed
    success_url = '/curriculums/'
    template_name = 'create_course_curriculum.html'
