from models import Author,Book,Library,Librarian

author = Author.objects.get(name=author_name)
book = Book.objects.filter(author=author)

books = Library.objects.get(name=library_name)
books = Library.books.all()

librarian = Librarian.objects.get(library=library_name)
