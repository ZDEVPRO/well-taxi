from django.contrib.auth.forms import UserCreationForm
from home.models import *
from django import forms


class NewUserForm(UserCreationForm):
    phone = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone', 'password1', 'password2']

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user
