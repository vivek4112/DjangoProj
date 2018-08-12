from django.contrib import admin
from .models import User, books, Review


admin.site.register(books)
admin.site.register(Review)
