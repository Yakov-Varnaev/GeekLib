from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from geeklib.service.paginator import paginate_queryset

from .models import Book, PublishsingHouse


class BooksListView(ListView):
    queryset = Book.objects.select_related('publisher')
    context_object_name = 'books'
    template_name = 'books/index.html'
    paginate_by = 10


class BookDetailView(DetailView):
    queryset = Book.objects.select_related('publisher')
    context_object_name = 'book'
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_libraries'] = paginate_queryset(
            self.request,
            self.object.available_libraries.select_related()
        )
        return context


class PublisherView(ListView):
    context_object_name = 'books'
    template_name = 'books/publisher.html'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        self.publisher = get_object_or_404(
            PublishsingHouse, id=self.kwargs.get('pk')
        )
        return self.publisher.books.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishing_house'] = self.publisher
        return context
