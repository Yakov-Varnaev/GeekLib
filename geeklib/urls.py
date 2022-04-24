from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('books:books-list'))),
    path('users/', include('users.urls', 'users')),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls', 'books')),
    path('libraries/', include('libraries.urls', 'libraries')),
]
