from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("one/", views.one, name="one"),
    path("two/", views.two, name="two"),
    path("files/<path:path>", views.files_path, name="files"),
    path("files/", views.files, name="files"),
    path("path/", views.waprfile, name="waprfile"),
]