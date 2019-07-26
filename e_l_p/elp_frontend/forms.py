from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class RegistrationForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = get_user_model()
        fields = ("username", "email", )

    def clean_password2(self):
        super().clean_password2()

    def _post_clean(self):
        super()._post_clean()

    def save(self):
        super().save()

class RegistrationFormModed(RegistrationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('Username', css_class='form-group col-md-6 mb-0'),
                Column('Email', css_class='form-group col-md-6 mb-0'),
                Column('password1', css_class='form-group col-md-6 mb-0'),
                Column('password2', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Sign up')
        )
