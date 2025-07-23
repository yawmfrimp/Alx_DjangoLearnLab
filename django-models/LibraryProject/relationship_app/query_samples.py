from models import Book,Library,Librarian


book = Book.objects.filter(author=author_name)

books = Library.objects.get(name=library_name)
books = Library.books.all()

librarian = Librarian.objects.get(library=library_name)
