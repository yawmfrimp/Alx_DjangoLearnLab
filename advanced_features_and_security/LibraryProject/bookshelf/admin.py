from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group , Permission

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields',{'fields':('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Fields', {'fields': ('date_of_birth',)})
    )
# Register your models here.
admin.site.register(Book, BookAdmin)

admin.site.register(CustomUser, CustomUserAdmin)

# creating or fetching the group
'''The following groups have been set up: editors, viewers, admins'''
Editors, created = Group.objects.get_or_create(name='Editors')
Viewers, created = Group.objects.get_or_create(name='Viewers')
Admins, created = Group.objects.get_or_create(name='Admins')

#fetch the permissions you want
'''The permissions created in views have been fetched into the variables
can_view_perm for the can_view permission, can_create_perm for the can_create permission
can_edit_perm for the can_edit_permission and the can_delete_perm for the can_delete_permission '''
can_view_perm  = Permission.objects.get(codename='can_view')
can_create_perm = Permission.objects.get(codename='can_create')
can_edit_perm = Permission.objects.get(codename='can_edit')
can_delete_perm = Permission.objects.get(codename='can_delete')

#assigning them to the group
'''The permissions fetched above are then assigned to the various groups created
editors get the can_view, can_create and can_edit permission, viewers get only the can_view permission
and the admins get all the permissions'''
Editors.permissions.add(can_create_perm,can_view_perm,can_edit_perm)
Viewers.permissions.add(can_view_perm)
Admins.permissions.add(can_create_perm,can_delete_perm,can_edit_perm,can_view_perm)
