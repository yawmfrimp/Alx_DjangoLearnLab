from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f'''title = {self.title}
        author = {self.author}
        publication_year = {self.publication_year}
'''
    class Meta:
        permissions = [
            ('can_view', 'Can view books available'),
            ('can_create', 'Can create new books'),
            ('can_edit', 'Can edit attributes of a book'),
            ('can_delete', 'Can delete a book'),
        ]
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