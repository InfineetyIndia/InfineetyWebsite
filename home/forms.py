from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models  import Users

class SignUpForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={ 'class': 'form-control', 'id':'email'}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control','id':'mobile'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id':'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','id': 'password2'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].label = "Confirm Password"

    class Meta:
        model= Users
        fields = ('email', 'phone_no', 'password1', 'password2')
