from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views import View

from instadupe.app.forms import AccountEditForm
from instadupe.app.models import Image, Profile


class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {
            'images': Image.objects.all(),
        })


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if username == 'favicon.ico':
            return redirect(reverse('home'))

        return render(request, 'profile.html', {
            'profile': Profile.objects.get(user__username=username),
        })


class AccountEditView(LoginRequiredMixin, View):
    fields = ('avatar', 'username', 'email', 'fullname', 'website', 'bio')

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        return render(
            request, 'settings.html', {
                'form':
                AccountEditForm(
                    initial={
                        field: getattr(profile, field)
                        for field in self.__class__.fields
                    }),
            })

    def post(self, request, *args, **kwargs):
        form = AccountEditForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            for field in self.__class__.fields:
                setattr(profile, field, form.cleaned_data[field])
            profile.save(commit=False)
            profile.user.save()
            return redirect(reverse('account_edit'))

        return render(request, 'settings.html', {'form': AccountEditForm()})
