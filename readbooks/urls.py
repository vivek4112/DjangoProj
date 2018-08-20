from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("book/", views.book, name="book"),
    path("Create_Review/", views.Create_Review, name="Create_Review")
]
