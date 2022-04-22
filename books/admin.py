from django.contrib import admin

from .models import Book, PublishsingHouse


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'publisher', 'pub_date')
    filter_fields = ('publisher', 'author')


@admin.register(PublishsingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
