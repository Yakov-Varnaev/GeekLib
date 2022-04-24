from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

User = get_user_model()


class ProfileView(ListView):
    context_object_name = 'books'
    template_name = 'users/profile.html'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        return self.request.user.rents.select_related()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user
        return context
