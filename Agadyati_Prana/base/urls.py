from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("business_unit/", views.business_unit, name="business_unit"),
    path("main_admin/", views.main_admin, name="admin_main"),
    path("booking/", views.booking, name="booking"),
    path("form_admin/", views.form_admin, name="form_main"),
    path("retreat/", views.retreat, name="retreat"),
    path("Offerings/", views.offering, name="offering")
]