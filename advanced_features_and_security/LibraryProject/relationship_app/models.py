from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
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


class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,date_of_birth,password=None):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff') or not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_staff=True and is_superuser=True ')
        
        return self.create_user(username, email, date_of_birth, password=password, **extra_fields)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    # Prompt for date_of_birth when running 'createsuperuser'
    REQUIRED_FIELDS = ['email','date_of_birth']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username