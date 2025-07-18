book = Book.objects.get(id=1) 
book.title = "Nineteen Eighty-Four"
book.save()
book.title
#expected output
'Nineteen Eighty-Four'
        