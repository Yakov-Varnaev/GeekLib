from django.contrib import admin

from libraries.models import BookRent, Library, LibraryBook


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')


class TenantsInline(admin.TabularInline):
    model = BookRent


@admin.register(LibraryBook)
class LibraryBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'library')
    inlines = (TenantsInline,)
    