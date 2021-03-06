from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from libraries.forms import RentForm

from .models import BookRent, LibraryBook


@method_decorator(login_required, 'dispatch')
class LibraryBookDetail(DetailView):
    queryset = LibraryBook.objects.select_related()
    context_object_name = 'library_book'
    template_name = 'libraries/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = self.object.book
        context['form'] = RentForm(self.request.POST or None)
        if self.request.user.is_authenticated:
            context['is_rented'] = BookRent.objects.filter(
                book=self.object, tenant=self.request.user
            ).exists()
        return context

    def post(self, request, pk, **kwargs):
        book = get_object_or_404(LibraryBook, id=pk)
        form = RentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.tenant = request.user
            instance.book = book
            instance.save()
        return redirect(reverse('libraries:books-detail', args=[pk]))


class BookRentDelete(DeleteView):
    model = BookRent
    success_url = reverse_lazy('books:books-list')
