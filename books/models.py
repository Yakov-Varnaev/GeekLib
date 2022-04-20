from django.db import models


class PublishsingHouse(models.Model):
    
    class Meta:
        verbose_name = 'Publishing House'
        verbose_name_plural = 'Publishing Houses'
        db_table = 'publishing_houses'

    name = models.CharField('publising house name', max_length=255)


class Book(models.Model):

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        db_table = 'books'

    name = models.CharField('book name', max_length=255)
    pub_date = models.DateField('Publishing Date')
    author = models.TextField('author`s name')
    publisher = models.ForeignKey(
        PublishsingHouse,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='Publisher'
    )
