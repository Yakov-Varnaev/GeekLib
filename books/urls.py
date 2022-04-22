from django.urls import path

from .views import BooksListView, PublisherView

app_name = 'books'

urlpatterns = [
    path('', BooksListView.as_view(), name='books-list'),
    path('publisher/<int:pk>/', PublisherView.as_view(), name='publishers-detail'),
]