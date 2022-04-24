from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Library(models.Model):

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'
        db_table = 'libraries'

    name = models.CharField('Library Name', max_length=255)
    address = models.TextField('Library address')
    books = models.ManyToManyField(
        'books.Book',
        related_name='libraries',
        verbose_name='library book',
        through='LibraryBook'
    )


class LibraryBook(models.Model):

    class Meta:
        verbose_name = 'Library Book'
        verbose_name_plural = 'Library Books'
        db_table = 'library_books'

    book = models.ForeignKey(
        'books.Book',
        on_delete=models.CASCADE,
        verbose_name='Book',
        related_name='available_libraries'
    )
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        verbose_name='Library'
    )
    amount = models.PositiveBigIntegerField('Books amount', default=0)
    tenants = models.ManyToManyField(
        User,
        related_name='rented_books',
        through='BookRent'
    )


class BookRent(models.Model):

    class Meta:
        verbose_name = 'Book Rent'
        verbose_name_plural = 'Book Rents'
        db_table = 'book_rents'

    book = models.ForeignKey(
        LibraryBook,
        on_delete=models.CASCADE,
        related_name='rents',
        verbose_name='rented book'
    )
    tenant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='rents',
        verbose_name='tenant'
    )
    to_date = models.DateField('Rent Expiration Date')
