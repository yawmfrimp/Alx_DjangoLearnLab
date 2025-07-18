l = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
Book: title = 1984
    author = George Orwell
    publication_year = 1949
l.save()
l.id
#expected output
1