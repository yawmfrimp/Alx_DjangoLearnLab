from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')


# Register your models here.
admin.site.register(Book, BookAdmin)

@admin.register(CustomUser)
class ModelAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields',{'fields':('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Fields', {'fields': ('date_of_birth',)})
    )