from django.views.generic import ListView, DetailView

from geeklib.service.paginator import paginate_queryset
from .models import Book, PublishsingHouse


class BooksListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name='books/index.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_libraries'] = paginate_queryset(self.request, self.object.available_libraries.all())
        return context


class PublisherView(DetailView):
    model = PublishsingHouse
    context_object_name = 'publishing_house'
    template_name = 'books/publisher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
