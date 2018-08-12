from django.urls import path

from . import views


urlpatterns = [
    path("index/", views.index, name="index"),
    path("book/", views.book, name="book"),
    path("Create_Review/", views.Create_Review, name="Create_Review")
]
