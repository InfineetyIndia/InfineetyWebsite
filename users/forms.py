from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models  import Users

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=60, required=True, help_text='Required. A valid Email address.')
    phone_no = forms.CharField(max_length=11, required=True, help_text=' Required. A valid Phone number')

    class Meta:
        model= Users
        fields = ('email', 'phone_no', 'password1', 'password2')
