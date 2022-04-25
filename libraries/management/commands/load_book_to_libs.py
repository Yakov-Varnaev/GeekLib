import random
from django.core.management import BaseCommand

from books.models import Book
from libraries.models import Library, LibraryBook


class Command(BaseCommand):

    def handle(self, *args, **options):
        books = Book.objects.all()
        libraries = Library.objects.all()

        for book in books:
            LibraryBook.objects.bulk_create([
                LibraryBook(book=book, library=library, amount=random.randint(1, 20))
                for library in libraries
            ])

        lib_book_count = LibraryBook.objects.count()
        return f'{lib_book_count} library books was added to db.'
