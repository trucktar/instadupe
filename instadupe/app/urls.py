from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import include, path
from django_registration.backends.activation.views import RegistrationView

from instadupe.app import views

# Account related URL patterns
accpatterns = [
    path('emailsignup/',
         RegistrationView.as_view(template_name='auth/signup.html'),
         name='signup'),
    path('login/',
         LoginView.as_view(template_name='auth/login.html'),
         name='login'),
    path('logout/', logout_then_login, name='logout'),
]

urlpatterns = [
    path('<profile_name>/', views.index, name='home'),
    path('accounts/', include(accpatterns)),
    path('accounts/edit/', views.edit_account, name='account_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
