from django.contrib import admin
from . import models 

class BookStoreAdminArea(admin.AdminSite):
    site_header = 'Bookstore Admin Area'

book_site = BookStoreAdminArea(name='BookstoreAdmin')

# blog_site.register(models.Post)