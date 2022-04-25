from django.contrib.auth.views import LoginView
from django.urls import include, path, reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm
from .views import ProfileView

app_name = 'users'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        'register/',
        CreateView.as_view(
            template_name='users/signup.html',
            form_class=SignupForm,
            success_url=reverse_lazy('books:books-list')
        ),
        name='signup'
    ),
    path('', include('django.contrib.auth.urls')),
]
