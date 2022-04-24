from django.urls import path

from .views import LibraryBookDetail

app_name = 'libraries'

urlpatterns = [
    path('book/<int:pk>/', LibraryBookDetail.as_view(), name='books-detail'),
]
