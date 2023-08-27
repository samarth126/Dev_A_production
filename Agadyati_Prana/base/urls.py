from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("main_admin/", views.main_admin, name="admin_main"),
    path("form_admin/", views.form_admin, name="form_main"),
]