from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field


STATES = (
    ('', 'Choose...'),
    ('Course1', 'CS1'),
    ('Course2', 'CS2'),
    ('Course3', 'CS3')
)

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



class CourseCurriculumBaseForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.TextInput())



class CurriculumPackageFormModed(CourseCurriculumBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('description', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Sign up')
        )


class CourseForm(CourseCurriculumBaseForm):
    CurriculumPackage = forms.ChoiceField(choices=STATES)



class CourseFormModed(CourseCurriculumBaseForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('state', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Sign up')
        )
        super().__init__(*args, **kwargs)

    # address_1 = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
    # address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}))
    # city = forms.CharField()
    # state = forms.ChoiceField(choices=STATES)
    # zip_code = forms.CharField(label='Zip')
    # check_me_out = forms.BooleanField(required=False)

# class CrispyAddressForm(AddressForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Column('email', css_class='form-group col-md-6 mb-0'),
#                 Column('password', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             'address_1',
#             'address_2',
#             Row(
#                 Column('city', css_class='form-group col-md-6 mb-0'),
#                 Column('state', css_class='form-group col-md-4 mb-0'),
#                 Column('zip_code', css_class='form-group col-md-2 mb-0'),
#                 css_class='form-row'
#             ),
#             'check_me_out',
#             Submit('submit', 'Sign in')
#         )


# class CustomCheckbox(Field):
#     template = 'custom_checkbox.html'


# class CustomFieldForm(AddressForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Column('email', css_class='form-group col-md-6 mb-0'),
#                 Column('password', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             'address_1',
#             'address_2',
#             Row(
#                 Column('city', css_class='form-group col-md-6 mb-0'),
#                 Column('state', css_class='form-group col-md-4 mb-0'),
#                 Column('zip_code', css_class='form-group col-md-2 mb-0'),
#                 css_class='form-row'
#             ),
#             CustomCheckbox('check_me_out'),
#             Submit('submit', 'Sign in')
#         )
