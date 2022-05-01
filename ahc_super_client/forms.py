from django import forms
from django.contrib.auth.forms import UserCreationForm

from ahc_app.models import User


class AddClientForm(UserCreationForm):
    username = forms.CharField(max_length=32, help_text='First name',widget=forms.TextInput(attrs={'placeholder': 'username'}))
    first_name = forms.CharField(max_length=32, help_text='First name',widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=32, help_text='Last name',widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=64,
                             help_text='Enter a valid email address',widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    mobile_number = forms.IntegerField(
        help_text='Enter a valid mobile number',widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}))
    password1 = forms.CharField(max_length=32, help_text='Password',
                                widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=32, help_text='Retype Password',
                                widget=forms.TextInput(attrs={'placeholder': 'Retype Password'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'mobile_number',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        if commit:
            user.save()
        return user


