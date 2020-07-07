from django import forms
from django.contrib.auth.models import User

from instadupe.app.models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'website', 'bio']


class AccountEditForm(UserEditForm, ProfileEditForm):
    fullname = forms.CharField(max_length=180)
