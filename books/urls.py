from django.urls import path

from .views import BookDetailView, BooksListView, PublisherView

app_name = 'books'

urlpatterns = [
    path('', BooksListView.as_view(), name='books-list'),
    path('<int:pk>/', BookDetailView.as_view(), name='books-detail'),
    path('publisher/<int:pk>/', PublisherView.as_view(), name='publishers-detail'),
]