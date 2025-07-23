from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book,Library

# Create your views here.
def list_books(request):
    """A function for viewing all books stored in the database."""
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)

class LibraryDetailView(DetailView):
    """ A class based view listing all details available for a specific library """
    model = Library