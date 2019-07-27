from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


from api.models.courses import Course
from .forms import (
    RegistrationFormModed,
    CurriculumPackageFormModed,
    CourseFormModed
)



def landing_page(request):
	return render(request, 'landing_page.html')


class SignUp(generic.CreateView):
    form_class = RegistrationFormModed
    success_url = 'elp/login/'
    template_name = 'signup.html'


class CurriculumView(LoginRequiredMixin, generic.edit.FormMixin):
    model = Course

    form_class = CurriculumPackageFormModed
    success_url = '/curriculums/'
    template_name = 'create_course_curriculum.html'
