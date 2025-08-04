views.py
the delete_model view:
This view is to delete an existing book, only users with the 'can_delete' permission can access this view

the create_model view:
This view is to create a new book, only users with the 'can_create' permission can access this view

def edit_model view
This view is to edit the attributes of an existing book, only users with the 'can_edit' permission can access this view

the view model view
This view is to view all existing books, only users with the 'can_view' permission can access this view

admin.py
The following groups have been set up: editors, viewers, admins
The permissions created in views have been fetched into the variables
can_view_perm for the can_view permission, can_create_perm for the can_create permission
can_edit_perm for the can_edit_permission and the can_delete_perm for the can_delete_permission
The permissions fetched above are then assigned to the various groups created
editors get the can_view, can_create and can_edit permission, viewers get only the can_view permission
and the admins get all the permissions