from django.contrib.auth import get_user_model
from django.views.generic import DetailView

User = get_user_model()


class ProfileView(DetailView):
    context_objetc_name = 'user'
    queryset = User.objects.prefetch_related('rents')
    template_name = 'users/profile.html'