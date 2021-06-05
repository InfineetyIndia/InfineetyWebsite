from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models  import Users

class SignUpForm(UserCreationForm):
    email = forms.CharField(error_messages={'required': 'Email should not be empty.'},max_length=60, required=True,  help_text='Required. A valid Email address.')
    phone_no = forms.CharField(error_messages={'required': 'Phone number should not be empty.', 'max_length':'Phone number should not be more than 10', 'max_length':'Phone number should not be less than 10'},max_length=10, min_length=10, required=True, help_text=' Required. A valid Phone number')

    class Meta:
        model= Users
        fields = ('email', 'phone_no', 'password1', 'password2')
