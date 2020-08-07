from django import forms
from extuser.models import ExtUser

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    new_password1 = forms.CharField(
        label=("Новый пароль"),
        widget=forms.PasswordInput,
        strip=False,
        required=False,
    )
    new_password2 = forms.CharField(
        label=("Повторите новый пароль"),
        strip=False,
        widget=forms.PasswordInput,
        required=False,
    )

    class Meta:
        model = ExtUser
        fields = ('first_name',
                  'second_name',
                  'last_name',
                  'email',
                  'phone',
                  'avatar',)
