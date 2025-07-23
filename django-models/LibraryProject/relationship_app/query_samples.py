from models import Book,Library,Librarian


book = Book.objects.filter(author='John Smith')

books = Library.books.all()

librarian = Librarian.objects.get(library='Library_name')
