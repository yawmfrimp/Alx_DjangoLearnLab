k = Book.objects.get(id=1) 
k.title = "Nineteen Eighty-Four"
k.save()
k.title
#expected output
'Nineteen Eighty-Four'
        