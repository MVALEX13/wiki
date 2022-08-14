from django.urls import path

from . import views

## app_name used to design the app urls from html file
app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.wiki_page, name = "wiki_page")
]
