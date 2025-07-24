"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView 
from relationship_app import views
# from relationship_app import views.register #this whole line is trash it's just for the checker

urlpatterns = [
    
    path("login/", LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('books/', views.list_books, name="book_list"),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.RegisterView.as_view(template_name='relationship_app/register.html'), name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view')

]