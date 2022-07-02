from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate
User = get_user_model()


class UserCreateForm(UserCreationForm):
    email = forms.EmailField()
    #is_seller = forms.BooleanField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

        def clean(self):
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(request, email=email, password=password):
                raise forms.ValidationError("Invlaid Login")


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    firstname = forms.CharField(max_length=85)
    lastname = forms.CharField(max_length=85)
    recovery_email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'recovery_email', 'img']
