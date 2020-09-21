from .models import Book
from django.views.generic import ListView


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 5
    template_name = 'books/book-list.html'
