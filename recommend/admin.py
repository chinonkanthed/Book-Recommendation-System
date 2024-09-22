from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'votes', 'read_url', 'buy_url')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)