from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()
#expected output
(1, {'bookshelf.Book': 1})
Book.objects.all()
#expected output
<QuerySet []>