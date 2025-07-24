from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    class Meta:
        permissions = [
            ('can_add_book', 'Can add books to the database' ),
            ('can_change_book', 'Can change the attributes of a book'),
            ('can_delete_book', 'Can delete books'),
        ]

    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def  __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} of {self.library}'
    
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='profile')
    
    ROLE_CHOICES = [
        ('Admin',  'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member', help_text="Role of the user in the system")

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"