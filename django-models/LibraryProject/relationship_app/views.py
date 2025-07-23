from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Library, Book



# Create your views here.
def list_books(request):
    """A function for viewing all books stored in the database."""
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """ A class based view listing all details available for a specific library """
    model = Library
    template_name = 'relationship_app/library_detail.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

