from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, reverse
from django.views import View

from instadupe.app.forms import AccountEditForm, ProfileEditForm
from instadupe.app.models import Image, Profile


class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'index.html',
            context={
                'profile': Profile.objects.get(user=request.user),
                'images': Image.objects.all(),
            },
        )


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')

        if username == 'favicon.ico':
            return redirect(reverse('home'))

        context = {'profile': Profile.get_profile(username=username)}
        if request.user.is_authenticated:
            context['profile_form'] = ProfileEditForm()

        return render(request, 'profile.html', context=context)

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)

        profile_form = ProfileEditForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if profile_form.is_valid():
            profile_form.save()

        return redirect(request.META.get('HTTP_REFERER'))


class AccountEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        account_inits = {
            field: getattr(profile, field)
            for field in ('username', 'email')
        }
        profile_inits = {
            field: getattr(profile, field)
            for field in ('avatar', 'fullname', 'website', 'bio')
        }

        return render(
            request,
            'accounts/edit-profile.html',
            context={
                'profile': profile,
                'profile_form': ProfileEditForm(initial=profile_inits),
                'account_form': AccountEditForm(initial=account_inits),
            },
        )

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)

        profile_form = ProfileEditForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if profile_form.is_valid():
            profile_form.save()

        account_form = AccountEditForm(request.POST, instance=request.user)
        if account_form.is_valid():
            account_form.save()

        return redirect(reverse('account-edit'))
