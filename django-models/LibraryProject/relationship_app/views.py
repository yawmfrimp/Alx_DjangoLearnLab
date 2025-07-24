from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import Library, Book, UserProfile
from django.contrib.auth.decorators import login_required, user_passes_test



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
    form_class = UserCreationForm() #in futute remove the brackets its a class not a function
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

def is_admin(user):
    if not user.is_authenticated:
        return False
    profile = getattr(user, 'profile', None)
    return bool(profile and profile.role == "Admin")

def is_member(user):
    if not user.is_authenticated:
        return False
    profile = getattr(user, 'profile', None)
    return bool(profile and profile.role == "Member")

def is_librarian(user):
    if not user.is_authenticated:
        return False
    profile = getattr(user, 'profile', None)
    return bool(profile and profile.role == "Librarian")

   
@login_required
@user_passes_test(is_admin, login_url='login', redirect_field_name=None)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian, login_url='login', redirect_field_name=None)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member, login_url='login', redirect_field_name=None)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
