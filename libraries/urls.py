from django.urls import path

from .views import BookRentDelete, LibraryBookDetail

app_name = 'libraries'

urlpatterns = [
    path('book/<int:pk>/', LibraryBookDetail.as_view(), name='books-detail'),
    path('book-rent/<int:pk>/return/', BookRentDelete.as_view(), name='book-return'),
]
