from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import include, path
from django_registration.backends.one_step.views import RegistrationView

from instadupe.app import views

# Account related URL patterns
accpatterns = [
    path(
        'emailsignup/',
        RegistrationView.as_view(
            template_name='accounts/signup.html',
            success_url='/',
        ),
        name='signup',
    ),
    path(
        'login/',
        LoginView.as_view(template_name='accounts/login.html'),
        name='login',
    ),
    path('logout/', logout_then_login, name='logout'),
    path('edit/', views.AccountEditView.as_view(), name='account-edit'),
]

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<username>/', views.ProfileView.as_view(), name='profile'),
    path('accounts/', include(accpatterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
