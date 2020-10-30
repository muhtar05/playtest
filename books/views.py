from django.shortcuts import render
from django.views.generic import View
from books.models import Book


class IndexView(View):

    def get(self, request, *args, **kwargs):
        ctx = {}
        ctx['books'] = Book.objects.all()
        return render(request, 'books/index.html', ctx)
