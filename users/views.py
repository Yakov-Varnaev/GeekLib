from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

User = get_user_model()


@method_decorator(login_required, 'dispatch')
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
