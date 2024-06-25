from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("searchEntry", views.searchEntry, name="searchEntry"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("randomPage", views.randomPage, name="randomPage"),
    path("NewPage", views.CreateNewPage, name="NewPage")
]
