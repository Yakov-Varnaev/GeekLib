from django.contrib.auth import get_user_model
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404

User = get_user_model()


class ProfileView(ListView):
    context_object_name = 'books'
    template_name = 'users/profile.html'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        self.profile = get_object_or_404(User, id=self.kwargs.get('pk'))
        return self.profile.rents.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context