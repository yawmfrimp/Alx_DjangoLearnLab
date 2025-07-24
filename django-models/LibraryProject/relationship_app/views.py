from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Library, Book, UserProfile
from django.forms import modelform_factory
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test 



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

'''An 'Admin' view that only users with the 'Admin' role can access.'''
@login_required
@user_passes_test(is_admin, login_url='login', redirect_field_name=None)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

'''A 'Librarian' view accessible only to users identified as 'Librarians'.'''
@login_required
@user_passes_test(is_librarian, login_url='login', redirect_field_name=None)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

'''A 'Memeber' view accessible only to users identified as 'Member'.'''
@login_required
@user_passes_test(is_member, login_url='login', redirect_field_name=None)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

BookForm = modelform_factory(Book, fields=['title', 'author'])

@login_required
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
        else:
            form = BookForm()

@login_required
@permission_required('relationship_app.can_change_book')
def edit_book(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'relationship_app/book_form.html', {
        'form' : form,
        'edit' : True,
        'book' : book,
    })


@login_required
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request,f'"{book.title}" was deleted.')
        return redirect('list_books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})    

    
