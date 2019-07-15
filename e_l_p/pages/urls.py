from django.urls import path
from .views import signup_signin

urlpatterns = [
	path('', signup_signin.landing_page, name='index'),
]