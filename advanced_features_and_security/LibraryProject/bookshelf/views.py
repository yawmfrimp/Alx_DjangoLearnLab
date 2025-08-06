from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.forms import modelform_factory
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import Book

# Create your views here.
@csrf_protect
def detail(request, book_id):
    return HttpResponse('You\'re looking at book %s.' % book_id)

BookForm = modelform_factory(Book, fields=['title', 'author', 'publication_year'])

@csrf_protect
def list_books(request):
    '''This view is to list all available books in the database'''
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'bookshelf/list_books.html', context)

@csrf_protect    
@permission_required('bookshelf.can_create', raise_exception=True)
def create_model(request):
    '''This view is to create a new book, only users with the 'can_create' permission can access this view'''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
        else:
            form = BookForm()
    return render(request, 'bookshelf/book_form.html',{'form': form})

@csrf_protect
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_model(request,pk):
    '''This view is to edit an existing book, only users with the 'can_edit' permission can access this view'''
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        if request.method == 'POST':
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect('list_books')
    else:
        form = BookForm(instance=book)
        return render(request, 'bookshelf/book_form.html', {
        'form' : form,
        'edit' : True,
        'book' : book,
    })

@csrf_protect
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_model(request,pk):
    '''This view is to delete an existing book, only users with the 'can_delete' permission can access this view'''    
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        messages.success(request,f'"{book.title}" was deleted.')
        return redirect('list_books')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})    


