from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book, PublishsingHouse


class BooksListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name='books/index.html'


class PublisherView(DetailView):
    model = PublishsingHouse
    context_object_name = 'publishing_house'
    template_name = 'books/publisher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
