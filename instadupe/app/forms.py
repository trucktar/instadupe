from django.contrib.auth.models import User
from django.forms import CharField, ModelForm

from instadupe.app.models import Profile


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'website', 'bio']

    fullname = CharField(max_length=180, required=False)


class AccountEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']
