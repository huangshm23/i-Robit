from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=6,max_length=12)
    