l = Book.objects.get(id=1)
l.delete()
#expected output
(1, {'bookshelf.Book': 1})
Book.objects.all()
#expected output
<QuerySet []>