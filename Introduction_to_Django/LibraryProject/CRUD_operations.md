create.md
l = Book(title="1984", author="George Orwell", publication_year=1949)
l.save()
l.id
#expected output
1

retrieve.md
Book.objects.get(id=1)

#expected output
title = 1984
author = George Orwell
publication_year = 1949

update.md
k = Book.objects.get(id=1) 
k.title = "Nineteen Eighty-Four"
k.save()
k.title
#expected output
'Nineteen Eighty-Four'

delete.md
l = Book.objects.get(id=1)
l.delete()
#expected output
(1, {'bookshelf.Book': 1})
Book.objects.all()
#expected output
<QuerySet []>